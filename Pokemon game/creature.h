#pragma once

#include "statuseffect.h"
#include <vector>
#include <string>
#include <QLabel>
/*
 * Matthew Graber, Cameron Luzadder, Katherine Newman
 * Parent class for the creature
 * Contains all the relevant details and functions, such as statistics, pointers to objects in the UI, etc
 */

#include <QProgressBar>

using namespace std;

#ifndef CREATURE_H
#define CREATURE_H


class Creature
{
public:
    Creature();
    Creature(int, int, int);

    //Pointers for output
    QLabel *mainlabel;
    QLabel *personalLabel;
    QProgressBar *healthBar;
    string *maindisplayQue;
    string personalDisplayQue;

    std::string name;   //Creature's name
    int maxHp;   //Hit point maximum
    int hp;      //Current hit points
    int ap;      //Attack power
    int armor;   //Damage reduction
    int level;   //Creature's current level
    int xp;      //Creature's current xp

    //Temporary modifiers
    TempMod tempHP;
    TempMod tempAP;
    TempMod tempArmor;
    TempMod persistentDamage;

    //Damage resistances, immunities, and weaknesses
    //Each vector<string> in the vector should hold two values
    //The first value should be the damage type (cold, fire, radiant, etc.)
    //The second should be how it affects the creature (vulnerable, resistant, immune, or special)
    std::vector<std::vector<std::string>> specialDamage;

    //Abilities
//    Ability* ability1;
//    Ability* ability2;
//    Ability* ability3;
//    Ability* ability4;
//    vector<Ability> lockedAbilities;
    virtual void ability1(Creature&){}
    virtual void ability2(Creature&){}
    virtual void ability3(Creature&){}
    virtual void ability4(Creature&){}
    string abilityNames[4];
    string abilityDescriptions[4];
    bool abilityUnlocked[4];

    //Getters
    virtual int getHp();
    virtual int getMaxHp();
    virtual int getAp();
    virtual int getArmor();

    //Setters
    virtual void takeDamage(int, string);
    virtual void heal(int);
    void earnXp(int);

    //Special damage type functions
    void addSpecialDamage(string, string);
    void addResistance(string);
    void addImmunity(string);
    void addVulnerability(string);
    void addRegenerative(string);

    //Other functions
    virtual void levelUp();
    virtual void endOfRound();
    virtual void endOfMatch();
    void addEffect(TempMod&, StatusEffect);  //Adds a new effect to the modifier
    void printDetails();
    void displayMessage(std::string);
    void pushQue();

    //Basic attack and overloaders
    //The creature passed into the function takes damage
    void basicAttack(Creature&);
    void basicAttack(Creature&, int);
    void basicAttack(Creature&, string);
    void basicAttack(Creature&, int, string);

};

#endif // CREATURE_H
