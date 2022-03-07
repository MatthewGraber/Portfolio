/*
 * Matthew Graber, Cameron Luzadder, Katherine Newman
 * The StatusEffect and TempMod classes
 * Used to keep track of any temporary effects that could be afflicting a creature
 */

#include "statuseffect.h"
#include "globalConstants.h"
#include <iostream>

#define DEBUG

//*********************************
//*******STATUSEFFECT CLASS********
//*********************************
//Constructors
StatusEffect::StatusEffect() : source(""), value(0), duration(0), stackable(true), permanent(false) {}
StatusEffect::StatusEffect(std::string sour, int v, int d, bool stack, bool per) : source(sour), value(v), duration(d), stackable(stack), permanent(per){

}

//Getters
std::string StatusEffect::getSource() {
    return source;
}
int StatusEffect::getDuration() {
    if (permanent) {
        return 999;
    }
    return duration;
}
int StatusEffect::getValue() {
    return value;
}
bool StatusEffect::isPermanent() {
    return permanent;
}
bool StatusEffect::isStackable() {
    return stackable;
}

//Setters
void StatusEffect::reduceDuration(int reduction) {
    duration -= reduction;
    if (duration <= 0 && !permanent) {
        value = 0;
        duration = 0;
#ifdef DEBUG
        cout << source << " ended.\n\n";
#endif

    }
}
void StatusEffect::setValue(int newValue) {
    value = newValue;
}

//Operator functions
StatusEffect operator + (StatusEffect const &obj1, StatusEffect const &obj2) {
    StatusEffect se;
    if (obj1.source == obj2.source) {
        if (obj1.stackable && obj2.stackable) {
            se.permanent = obj1.permanent + obj2.permanent;
            se.stackable = true;
            se.duration = obj1.duration + obj2.duration;
            se.value = obj1.value + obj2.value;
        }
    }
    return se;
}


//*********************************
//*********TEMPMOD CLASS***********
//*********************************

//Removes all status effects
void TempMod::clear() {
    effects.clear();
}

//Removes all non-permanent status effects
void TempMod::endOfMatch(){
    for (int i = 0; i < effects.size(); i++) {
        if (!effects[i].isPermanent()) {
            effects.erase(effects.begin()+i);
            i--;
        }
    }
}

//Checks all the effects and removes ones that have ended
void TempMod::endOfRound() {
    for (StatusEffect &se : effects) {
        if (se.getDuration() > 0) {
            se.reduceDuration(1);
        }
    }
    for (int i = effects.size()-1; i >=0; i--) {
        if (effects[i].getDuration() == 0) {
            effects.erase(effects.begin()+i);
        }
    }
}

//Add a new status efect to the list
void TempMod::addEffect(StatusEffect se) {
    effects.push_back(se);
}

//Returns the total modifer
int TempMod::getMod() {
    int total = 0;
    for (StatusEffect se : effects) {
        total += se.getValue();
    }
    return total;
}
