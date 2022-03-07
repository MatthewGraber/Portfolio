/*
 * Matthew Graber, Cameron Luzadder, Katherine Newman
 * Parent class for the creature
 * Contains all the relevant details and functions, such as statistics, pointers to objects in the UI, etc
 */

#include "creature.h"
#include <iostream>
#include "globalConstants.h"
#include <string>
#include <vector>
#include <chrono>
#include <thread>

#define DEBUG

using namespace std::this_thread; // sleep_for
using namespace std::chrono; // nanoseconds
using namespace std;

//*********************************
//********CREATURE CLASS***********
//*********************************

//Constructors
Creature::Creature()
{
    //Initalizing variables
    maxHp = 20;
    hp = maxHp;
    ap = 8;
    armor = 3;
    xp = 0;
    level = 1;

    //Temporary modifier objects
    tempAP = TempMod();
    tempArmor = TempMod();
    tempHP = TempMod();
    persistentDamage = TempMod();
}

//Basic constructor
Creature::Creature(int hpMax, int attack, int arm) {
    Creature();
    maxHp = hpMax;
    hp = maxHp;
    ap = attack;
    armor = arm;
}

//Public variables and functions
//Getters
int Creature::getHp() {
   return hp;
}
int Creature::getMaxHp() {
    int n = maxHp + tempHP.getMod();
    if (n < 0) { return 0; }
    return n;
}
int Creature::getAp() {
    int n = ap + tempAP.getMod();
    if (n < 0) { return 0; }
    return n;
}
int Creature::getArmor() {
    int n = armor + tempArmor.getMod();
    if (n < 0) { return 0; }
    return n;
}

//Setters
//Deals damage to the creature
//If the creature has any special resistances or anything to the damage type, that will change the amount of damage they take
///@param damage damage the creature takes
void Creature::takeDamage(int damage, string type) {
    string special = "";

    if (type != "Healing") {
        //Checks to see if the damage type is on the creature's special list
        for (int i = 0; i < specialDamage.size(); i++) {
            if (type == specialDamage[i][0]) {
                special = specialDamage[i][1];
                break;
            }
        }

        //Determines what to do with the damage type
        if (special == "Immune") {
            return;
        }
        else if (special == "Resistant") {
            damage = damage*RESISTANT;
        }
        else if (special == "Vulnerable") {
            damage = damage*VULNERABLE;
        }
        else if (special == "Regenerative") {
            heal(damage);
            return;
        }

        //Checks to see if the armor is greater than the damage to ensure we don't heal via negative damage
        if (getArmor() > damage) { return; }

        hp -= (damage-getArmor());

#ifdef DEBUG
cout << name << " took " << damage-getArmor() << " damage!\n\n";
#endif
displayMessage(name + " took " + to_string(damage-getArmor()) + " damage!");
    }
    else {
        hp += damage;
#ifdef DEBUG
cout << name << " healed " << damage << " damage!\n\n";
#endif
    displayMessage(name + " healed " + to_string(damage) + "HP");
    }
    if (hp > getMaxHp()) { hp = getMaxHp(); }
    else if (hp < 0) { hp = 0; }
    healthBar->setValue(hp);
}
//Heals the creature
void Creature::heal(int healing) {
   takeDamage(healing, "Healing");    //Healing is just reverse damage, after all
}
//Increases the character's xp and checks for a level up
void Creature::earnXp(int n) {
    xp += n;
    if (xp >= level) {
        xp -= level;
        levelUp();
    }
}


//Special damage type adders
void Creature::addSpecialDamage(string damageType, string effect) {
    vector<string> newType;
    newType.push_back(damageType);
    newType.push_back(effect);
    specialDamage.push_back(newType);
}
void Creature::addImmunity(string damageType) {
    addSpecialDamage(damageType, "Immune");
}
void Creature::addRegenerative(string damageType) {
    addSpecialDamage(damageType, "Regenerative");
}
void Creature::addResistance(string damageType) {
    addSpecialDamage(damageType, "Resistant");
}
void Creature::addVulnerability(string damageType) {
    addSpecialDamage(damageType, "Vulnerable");
}


//Basic attacks and their overloaders
void Creature::basicAttack(Creature &enemy, int damage, string type) {
    enemy.takeDamage(damage, type);
}
void Creature::basicAttack(Creature &enemy, string type) {
    basicAttack(enemy, getAp(), type);
}
void Creature::basicAttack(Creature &enemy, int damage) {
    basicAttack(enemy, damage, "Physical");
}
void Creature::basicAttack(Creature &enemy) {
    basicAttack(enemy, getAp(), "Physical");
}

//Other functions
//Increases the creature's level and increases their stats
void Creature::levelUp() {
    //Determines the level-up reward based on current level
    switch (level%3) {
    case 1:
        ap += 1;
        break;

    case 2:
        armor += 1;
        break;

    case 0:
        maxHp += 5;
        break;
    //Increases level
    level++;
    }

}

//Deals any persistent damage and reduces the duration of all temporary effects
void Creature::endOfRound() {
    //Deal persistent damage
    for (StatusEffect se : persistentDamage.effects) {
#ifdef DEBUG
        cout << "Dealing persistent " << se.getSource() << " damage!\n";
#endif
        takeDamage(se.getValue(), se.getSource());
    }

    //Reduce all effects
    persistentDamage.endOfRound();
    tempAP.endOfRound();
    tempArmor.endOfRound();
    tempHP.endOfRound();
    takeDamage(0, "Untyped");   //In case their hp max just went down
}

//Removes all temporary effects and rewards the creature with 1 xp
void Creature::endOfMatch() {
    persistentDamage.endOfMatch();
    tempAP.endOfMatch();
    tempArmor.endOfMatch();
    tempHP.endOfMatch();
    takeDamage(0, "Untyped");
    earnXp(1);
}

//A function to add new effects to the temporary modifier
//If the creature is immune to that type of effect, it will ignore it
void Creature::addEffect (TempMod &mod, StatusEffect newEffect) {
    for (vector<string> type : specialDamage) {
        if (type[0] == newEffect.getSource()) {
            if (type[1] == "Immune") {
                return;
            }
            else if (type[1] == "Resistant") {
                newEffect.setValue(newEffect.getValue()*RESISTANT);
            }
            else if (type[1] == "Vulnerable") {
                newEffect.setValue(newEffect.getValue()*VULNERABLE);
            }
        }
    }
    for (StatusEffect &se : mod.effects) {
        if (se.getSource() == newEffect.getSource()) {
            se = se+newEffect;
            return;
        }
    }
#ifdef DEBUG
cout << name << " gained status effect: " << newEffect.getSource() << "\n\n";
#endif
    mod.addEffect(newEffect);
}

//Displays all of the creature's information
void Creature::printDetails() {

    personalDisplayQue = "Name: "+name+"\n";
    personalDisplayQue = personalDisplayQue + "Current hp: " + to_string(getHp()) + "\n";
    personalDisplayQue = personalDisplayQue + "Attack: " + to_string(getAp()) + "\n";
    personalDisplayQue = personalDisplayQue + "Defense: " + to_string(getArmor());
    QString qstr = QString::fromStdString(personalDisplayQue);
    personalLabel->setText(qstr);

    healthBar->setMaximum(getMaxHp());
    healthBar->setValue(hp);

}

//Adds a message to the global que
void Creature::displayMessage(std::string message) {
    *maindisplayQue = *maindisplayQue + message + "\n";
}

//Displays all messages in the que
void Creature::pushQue() {
    QString qstr = QString::fromStdString(*maindisplayQue);
    mainlabel->setText(qstr);
    *maindisplayQue = "";
}
