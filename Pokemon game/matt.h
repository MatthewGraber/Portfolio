/*
 * Matthew Graber, Cameron Luzadder, Katherine Newman
 * A great and powerful creature know as a "Matt"
 * Child class of Creature
 * Contains definitions for their abilities, along with their descriptions and starting statistics
 */

#pragma once

#include "creature.h"
#ifndef MATT_H
#define MATT_H


class Matt : public Creature
{
public:
    Matt();
    void ability1(Creature&);
    void ability2(Creature&);
    void ability3(Creature&);
    void ability4(Creature&);
};

#endif // MATT_H
