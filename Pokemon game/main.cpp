/*
 * Matthew Graber, Cameron Luzadder, Katherine Newman
 * Main function
 * Calls the GUI and then doesn't do anything
 */

#define DEBUG

#include "mainwindow.h"
#include <QApplication>
#include <iostream>
#include "creature.h"
#include "matt.h"
#include "beholder.h"
#include "battle.h"
#include "globalVariables.h"

using namespace std;
//Creature* realMatt;
Matt matt;
//Creature* evilMatt;
Beholder beholder;
Matt mattAgain;
//Battle battle;
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;

    w.show();

    //battle.fight(*realMatt, *evilMatt, 1);

    return a.exec();
}
