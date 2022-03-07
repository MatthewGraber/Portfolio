/*
 * Matthew Graber, Cameron Luzadder, Katherine Newman
 * The StatusEffect and TempMod classes
 * Used to keep track of any temporary effects that could be afflicting a creature
 */

#pragma once

#include <string>
#include <vector>

#ifndef STATUSEFFECT_H
#define STATUSEFFECT_H

using namespace std;

class StatusEffect {
public:
    StatusEffect();
    StatusEffect(string, int, int, bool, bool);

    //Getters
    string getSource();
    int getValue();
    int getDuration();
    bool isStackable();
    bool isPermanent();

    //Setters
    void reduceDuration(int);
    void setValue(int);

    //Operator functions
    friend StatusEffect operator + (StatusEffect const &, StatusEffect const &);

private:
    string source;    //Where the effect came from
    int value, duration;    //For the duration, use 999 to indicate the entire round
    bool stackable, permanent; //Whether or not the effect can be stacked with an effect of the same name, and whether or not the effect is permanent

};

class TempMod {
public:
    vector<StatusEffect> effects;

    //Removes all status effects
    void clear();

    //Removes all non-permanent status effects
    void endOfMatch();

    //Checks all the effects and removes ones that have ended
    void endOfRound();

    //Returns the total modifer
    int getMod();

    //Adds a new status effect
    void addEffect(StatusEffect);

};


#endif // STATUSEFFECT_H
