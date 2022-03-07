/*
 * Matthew Graber, Cameron Luzadder, Katherine Newman
 * A great and powerful creature know as a "Matt"
 * Child class of Creature
 * Contains definitions for their abilities, along with their descriptions and starting statistics
 */

#include "matt.h"
#include <vector>

using namespace std;

Matt::Matt() : Creature(40, 7, 3)
{
    name = "Matt";
    vector<string> fireResistance;
    //addResistance("Fire");
    addImmunity("Psychic");
    addVulnerability("Physical");
    addRegenerative("Lightning");

    //Ability names and descriptions
    abilityNames[0] = "Fireball";
    abilityDescriptions[0] = "Immediately deal some fire damage, plus persistent fire damage";
    abilityUnlocked[0] = true;

    abilityNames[1] = "Slow";
    abilityDescriptions[1] = "Reduce the speed at which the opponent moves through time, reducing their attack and defense by 1";
    abilityUnlocked[1] = true;

    abilityNames[2] = "Haste";
    abilityDescriptions[2] = "Speed up time for yourself, increasing your attack and defense by 1";
    abilityUnlocked[2] = false;

    abilityNames[3] = "Double strike";
    abilityDescriptions[3] = "Make two attacks in rapid succession";
    abilityUnlocked[3] = false;

}
//Fireball attack
void Matt::ability1(Creature &target) {
    basicAttack(target, "Fire");
    StatusEffect se("Fire", getAp(), getAp()/2, false, false);
    target.addEffect(target.persistentDamage, se);
}
//Slowing attack
void Matt::ability2(Creature &target) {
    StatusEffect se("Slow", -1, getAp(), true, false);
    target.addEffect(target.tempAP, se);
    target.addEffect(target.tempArmor, se);
}
//Hasting buff
void Matt::ability3(Creature &target) {
    StatusEffect se("Haste", 1, getAp(), true, false);
    addEffect(tempAP, se);
    addEffect(tempArmor, se);
}
//Double strike
void Matt::ability4(Creature &target) {
    basicAttack(target);
    basicAttack(target);
}
