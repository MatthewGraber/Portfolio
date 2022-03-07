/*
 * Matthew Graber, Cameron Luzadder, Katherine Newman
 * Made to run a single round of combat between the player and the opponent
 */

#ifndef BATTLE_H
#define BATTLE_H

#include "creature.h"

class Battle {
public:
    Battle() {}
    void fight(Creature &player, Creature &enemy, int num);

};

#endif // BATTLE_H
