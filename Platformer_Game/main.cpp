#include "mainwindow.h"
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <math.h>
#include <time.h>
#include <windows.h>
#include <ctime>
#include <cstdlib>
#include <QApplication>
#include <SFML/Window.hpp>
#include <SFML/Audio.hpp>
#include <SFML/Graphics.hpp>

//https://www.sfml-dev.org/tutorials/2.5/

using namespace sf;
using namespace std;
using namespace Style;

const double PI = atan(1) * 4;

const float GRID_SIZE = 50;

const string FILE_DIRECTORY = "C:\\Users\\Count Matthias VII\\Documents\\GitHub\\Game\\Platformer_Game\\Graphics";
const string PATH_BANANA = FILE_DIRECTORY + "\\Bananaman.jpg";
const string PATH_GRASS = FILE_DIRECTORY + "\\Grass.png";


const int WINDOW_X = 1200;
const int WINDOW_Y = 800;

//All the pretty colors!
const Color BLACK = Color::Black;
const Color BLUE = Color::Blue;
const Color CYAN = Color::Cyan;
const Color GREEN = Color::Green;
const Color MAGENTA = Color::Magenta;
const Color RED = Color::Red;
const Color TRANSPARENT_SF = Color::Transparent;
const Color WHITE = Color::White;
const Color YELLOW = Color::Yellow;


RectangleShape player;
const float PLAYER_X_ACCELERATION = 0.3;
const float PLAYER_X_DECELERATION = 0.1;
const float PLAYER_MAX_X_SPEED = 6;

const float PLAYER_Y_ACCELERATION = 4;
//const float PLAYER_Y_DECELERATION = 3;
const float PLAYER_MAX_Y_SPEED = 6;

const float GRAVITY = 0.1;
Vector2f playerVelocity;
const int MAX_JUMPTIME = 30;
int currentJumptime = 0;
int jumpsRemaining = 1;
bool inAir = false;

//Walls
vector<RectangleShape> walls;
void newWall(int, int, int, int, Color color = RED);

int main(int argc, char *argv[]) {
    srand(time(NULL));

    RenderWindow window;
    window.create(VideoMode(WINDOW_X, WINDOW_Y), "Game", (Close | Titlebar));
    window.setFramerateLimit(120);

    // Threads (none)


    //Player
    player.setFillColor(GREEN);
    player.setSize(Vector2f(GRID_SIZE, GRID_SIZE));

    FloatRect playerBounds = player.getGlobalBounds();

    //Walls
    newWall(1,1,5,2);
    newWall(2,1,10,10);

    //Collision
    FloatRect nextPos;


    while (window.isOpen()) {
        Event event;

        while (window.pollEvent(event)) {
            switch (event.type) {
                case Event::Closed:
                    window.close();
                    break;

            }


        }

        playerBounds = player.getGlobalBounds();


        //Player movement
//        playerVelocity.x = 0;
//        playerVelocity.y = 0;


        if (Keyboard::isKeyPressed(Keyboard::W)) {
            if (!inAir) {
                playerVelocity.y -= PLAYER_Y_ACCELERATION;
                currentJumptime = 0;
            }
            if ((inAir && currentJumptime < MAX_JUMPTIME)) {
                playerVelocity.y -= PLAYER_Y_ACCELERATION;
                currentJumptime++;
            }
            else {
                //currentJumptime = MAX_JUMPTIME;
                playerVelocity.y += GRAVITY;
            }
        }
        else {
            currentJumptime = MAX_JUMPTIME;
            playerVelocity.y += GRAVITY;
        }
        if (Keyboard::isKeyPressed(Keyboard::A) != Keyboard::isKeyPressed(Keyboard::D)) {
            if (Keyboard::isKeyPressed(Keyboard::D)) {
                playerVelocity.x += PLAYER_X_ACCELERATION;
            }
            else {
                playerVelocity.x -= PLAYER_X_ACCELERATION;
            }

        }
        else {
            float reduction = PLAYER_X_DECELERATION;

            //If the current velocity is less than the deceleration value, use the velocity as that value instead
            if (abs(playerVelocity.x) < PLAYER_X_DECELERATION) {
                reduction = abs(playerVelocity.x);
            }
            if (playerVelocity.x > 0) {
                playerVelocity.x -= reduction;
            }
            else {
                playerVelocity.x += reduction;
            }
        }


//        if (Keyboard::isKeyPressed(Keyboard::S)) {
//            playerVelocity.y += PLAYER_SPEED;
//        }


        if (playerVelocity.x > PLAYER_MAX_X_SPEED) {
            playerVelocity.x = PLAYER_MAX_X_SPEED;
        }
        else if (playerVelocity.x < -PLAYER_MAX_X_SPEED) {
            playerVelocity.x = -PLAYER_MAX_X_SPEED;
        }

        if (playerVelocity.y > PLAYER_MAX_Y_SPEED) {
            playerVelocity.y = PLAYER_MAX_Y_SPEED;
        }
        else if (playerVelocity.y < -PLAYER_MAX_Y_SPEED) {
            playerVelocity.y = -PLAYER_MAX_Y_SPEED;
        }

        //Resets the inAir variable
        inAir = true;

        //Collison
        for (auto &wall : walls) {
            FloatRect wallBounds = wall.getGlobalBounds();

            nextPos = playerBounds;
            //nextPos = player.getGlobalBounds();
            nextPos.left += playerVelocity.x;
            nextPos.top += playerVelocity.y;


//            nextPos.left = playerBounds.left + playerVelocity.x;
//            nextPos.top = playerBounds.top + playerVelocity.y;
            if (wallBounds.intersects(nextPos)) {
                //Side collision
                if ((playerBounds.left  + playerBounds.width <= wallBounds.left
                        || playerBounds.left >= wallBounds.left + wallBounds.width)) {
                    if (playerBounds.left + playerBounds.width <= wallBounds.left) {
                        playerVelocity.x = wallBounds.left - (playerBounds.left + playerBounds.width);
                    }
                    else {
                        playerVelocity.x = -(playerBounds.left - (wallBounds.left + wallBounds.width));
                    }

                }
                //Top or bottom collision
                if (playerBounds.top  + playerBounds.height <= wallBounds.top
                    || playerBounds.top >= wallBounds.top + wallBounds.height) {
                    //playerVelocity.y = 0;
                    if (playerBounds.top + playerBounds.height <= wallBounds.top) {
                        playerVelocity.y = wallBounds.top - (playerBounds.top + playerBounds.height);
                        inAir = false;
                    }
                    else {
                        playerVelocity.y = (playerBounds.top - (wallBounds.top + wallBounds.height));
                    }
                }





//                //Top collision
//                if (playerBounds.top > wallBounds.top + wallBounds.height
//                        && nextPos.top <= wallBounds.top + wallBounds.height) {
//                    //Triggers when the top of the player moves through the bottom of the box
//                    playerVelocity.y = playerBounds.top - (wallBounds.top + wallBounds.height); //Sets the player velocity so that it should line up with the box exactly
//                }
            }

        }

        player.move(playerVelocity);

        //Screen collision
        //Left collision
        if (player.getPosition().x < 0) {
            player.setPosition(0, player.getPosition().y);
            playerVelocity.x = 0;
        }
        //Top collision
        if (player.getPosition().y < 0) {
            player.setPosition(player.getPosition().x, 0);
            playerVelocity.y = 0;
        }
        //Right collision
        if (player.getPosition().x + player.getLocalBounds().width > WINDOW_X) {
            player.setPosition(WINDOW_X-player.getLocalBounds().width, player.getPosition().y);
            playerVelocity.x = 0;
        }
        //Bottom collision
        if (player.getPosition().y + player.getLocalBounds().height > WINDOW_Y) {
            player.setPosition(player.getPosition().x, WINDOW_Y-player.getLocalBounds().height);
            playerVelocity.y = 0;
            inAir = false;
        }

        // DRAW STUFF HERE
        window.clear(BLACK);

        window.draw(player);

        //Draws all the walls
        for (auto &i : walls) {
            window.draw(i);
        }

        window.display();
    }

    return 0;
}

void newWall(int sizeX, int sizeY, int posX, int posY, Color color) {
    RectangleShape wall;

    wall.setFillColor(color);
    wall.setSize(Vector2f(GRID_SIZE*sizeX, GRID_SIZE*sizeY));
    wall.setPosition(GRID_SIZE*posX, GRID_SIZE*posY);

    walls.push_back(wall);
}

