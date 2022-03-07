/*
 * Matthew Graber, Cameron Luzadder, Katherine Newman
 * Made to run a single round of combat between the player and the opponent
 */

#include <iostream>
#include <ctime>
#include <cstdlib>
#include "creature.h"
#include "battle.h"

using namespace std;

//Runs a single round of combat between the player and the enemy
void Battle::fight(Creature &player, Creature &enemy, int Attack_Choice)
{

//    Creature* player;
//    Matt matt;
//    player = &matt;

//    Creature* enemy;
//    Beholder beholder;
//    enemy = &beholder;

    int
    Turn = 0,
    //Attack_Choice,
    Computer_Attack,
    Player_Attack1Qty = 10,
    Player_Attack2Qty = 10,
    Player_Attack3Qty = 10,
    Player_HealQty = 10;
    bool deadPlayer = false;


    srand(static_cast<int>(time(0)));

    if(Turn == 0)// Player Turn
    {
        bool validInput = false;


        while (!validInput)
        {
            cout << "\nPick an attack. <1> <2> <3> or <4>:\n";
            cout << "1. " << player.abilityDescriptions[0] << " \n";
            cout << "2. " << player.abilityDescriptions[1] << " \n";
            cout << "3. " << player.abilityDescriptions[2] << " \n";
            cout << "4. " << player.abilityDescriptions[3] << " \n";
            cin >> Attack_Choice;

            if (Attack_Choice > 4 || Attack_Choice < 1)
            {
                cout << "\nInvalid choice! Please try again!\n";
                cin.ignore();
            }
            else if (Attack_Choice == 1 && Player_Attack1Qty == 0)
            {
                cout << "\nQuantity of Attack 1 has ran out! Select another move!\n";
            }
            else if (Attack_Choice == 2 && Player_Attack2Qty == 0)
            {
                cout << "\nQuantity of Attack 2 has ran out! Select another move!\n";
            }
            else if (Attack_Choice == 3 && Player_Attack3Qty == 0)
            {
                cout << "\nQuantity of Attack 3 has ran out! Select another move!\n";
            }
            else if (Attack_Choice == 4 && Player_HealQty == 0)
            {
                cout << "\nQuantity of Heal has ran out! Select another move!\n";
            }
            else
            {
                validInput = true;
            }
        }

        player.displayMessage("You used " + player.abilityNames[Attack_Choice-1]);
        switch(Attack_Choice)
        {

            case 1: // player chooses to use ability 1
                cout << "\nYou chose " << player.abilityNames[0] << endl;
                player.ability1(enemy);
                break;


            case 2: // player chooses to use ability 2
                cout << "\nYou chose " << player.abilityNames[1] << endl;
                player.ability2(enemy);
                break;

            case 3: // player uses ability 3
                cout << "\nYou chose " << player.abilityNames[2] << endl;
                player.ability3(enemy);
                break;

            case 4: // player uses ability 4
                cout << "\nYou chose " << player.abilityNames[3] << endl;
                player.ability4(enemy);
                break;
        }
        player.endOfRound();
        player.printDetails();
        enemy.printDetails();

    }

    // check if any player has died
    if (player.getHp() == 0 || enemy.getHp() == 0)
    {
        deadPlayer = true;
    }

    if (!deadPlayer)
    {
        Computer_Attack = rand() % (4-1+1) + 1;
        enemy.displayMessage(enemy.name + " used " + enemy.abilityNames[Computer_Attack-1]);
        switch(Computer_Attack)
        {

            case 1:

                cout << "\n" << enemy.name << " used " << enemy.abilityNames[0] << endl;
                enemy.ability1(player);
                break;

            case 2:
                cout << "\n" << enemy.name << " used " << enemy.abilityNames[1] << endl;
                enemy.ability2(player);
                break;

            case 3:
                cout << "\n" << enemy.name << " used " << enemy.abilityNames[2] << endl;
                enemy.ability3(player);
                break;

            case 4:
                cout << "\n" << enemy.name << " used " << enemy.abilityNames[3] << endl;
                enemy.ability4(player);
                break;

        }
        enemy.endOfRound();
        player.printDetails();
        enemy.printDetails();
        player.pushQue();   //Only push the que from one of the creatures
    }

    //If the enemy is killed
    if (enemy.getHp() == 0) {
        enemy.endOfMatch();
        player.endOfMatch();
        cout << "Congratulations! You won!" << endl;

    }

    //If the player is killed
    if (player.getHp() == 0) {
        enemy.endOfMatch();
        player.endOfMatch();
        cout << "Your fighter has fainted! Game over!" << endl;
    }

}
