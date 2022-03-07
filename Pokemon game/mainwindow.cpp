/*
 * Matthew Graber, Cameron Luzadder, Katherine Newman
 * Runs the GUI
 */


#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include <QDebug>
#include <iostream>
#include "creature.h"
#include "matt.h"
#include "beholder.h"
#include "battle.h"
#include "globalVariables.h"

using namespace std;

Battle battle;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    realMatt = new Matt();
    evilMatt = new Matt();
    run();

}

MainWindow::~MainWindow()
{
    delete ui;

}

//Run when their respective buttons are clicked
void MainWindow::on_pushButton_clicked()
{
    battle.fight(*realMatt, *evilMatt, 1);
    if (evilMatt->getHp() == 0) {
        evilMatt->endOfMatch();
        realMatt->endOfMatch();
        QMessageBox::StandardButton reply = QMessageBox::warning(this, "Victory!", "You won!");
        QApplication::quit();
    }

    //If the player is killed
    if (realMatt->getHp() == 0) {
        evilMatt->endOfMatch();
        realMatt->endOfMatch();
        QMessageBox::StandardButton reply = QMessageBox::warning(this, "Game over", "You have been defeated.");
        QApplication::quit();
    }
}
void MainWindow::on_pushButton_2_clicked()
{
    battle.fight(*realMatt, *evilMatt, 2);
    if (evilMatt->getHp() == 0) {
        evilMatt->endOfMatch();
        realMatt->endOfMatch();
        QMessageBox::StandardButton reply = QMessageBox::warning(this, "Victory!", "You won!");
        QApplication::quit();
    }

    //If the player is killed
    if (realMatt->getHp() == 0) {
        evilMatt->endOfMatch();
        realMatt->endOfMatch();
        QMessageBox::StandardButton reply = QMessageBox::warning(this, "Game over", "You have been defeated.");
        QApplication::quit();
    }
}


void MainWindow::on_pushButton_3_clicked()
{
    battle.fight(*realMatt, *evilMatt, 3);
    if (evilMatt->getHp() == 0) {
        evilMatt->endOfMatch();
        realMatt->endOfMatch();
        QMessageBox::StandardButton reply = QMessageBox::warning(this, "Victory!", "You won!");
        QApplication::quit();
    }

    //If the player is killed
    if (realMatt->getHp() == 0) {
        evilMatt->endOfMatch();
        realMatt->endOfMatch();
        QMessageBox::StandardButton reply = QMessageBox::warning(this, "Game over", "You have been defeated.");
        QApplication::quit();
    }
}


void MainWindow::on_pushButton_4_clicked()
{
    battle.fight(*realMatt, *evilMatt, 4);
    if (evilMatt->getHp() == 0) {
        evilMatt->endOfMatch();
        realMatt->endOfMatch();
        QMessageBox::StandardButton reply = QMessageBox::warning(this, "Victory!", "You won!");
        QApplication::quit();
    }

    //If the player is killed
    if (realMatt->getHp() == 0) {
        evilMatt->endOfMatch();
        realMatt->endOfMatch();
        QMessageBox::StandardButton reply = QMessageBox::warning(this, "Game over", "You have been defeated.");
        QApplication::quit();
    }
}


void MainWindow::on_progressBar_valueChanged(int value)
{

}

//Runs all the neccessary initialization
void MainWindow::run() {
    string *que = new string;
    *que = "";
//    player = new Matt();
//    //evilMatt = &beholder;
//    enemy = new Matt();
    ui->setupUi(this);

    realMatt->mainlabel = ui->mainDisplay;
    realMatt->personalLabel = ui->playerDisplay;
    realMatt->healthBar = ui->playerHealth;
    realMatt->maindisplayQue = que;

    evilMatt->mainlabel = ui->mainDisplay;
    evilMatt->personalLabel = ui->enemyDisplay;
    evilMatt->healthBar = ui->enemyHealth;
    evilMatt->maindisplayQue = que;
    evilMatt->name = "Evil Matt";

    realMatt->printDetails();
    evilMatt->printDetails();

    string str = realMatt->abilityNames[0];
    QString qstr = QString::fromStdString(str);
    ui->pushButton->setText(qstr);

    str = realMatt->abilityNames[1];
    qstr = QString::fromStdString(str);
    ui->pushButton_2->setText(qstr);

    str = realMatt->abilityNames[2];
    qstr = QString::fromStdString(str);
    ui->pushButton_3->setText(qstr);

    str = realMatt->abilityNames[3];
    qstr = QString::fromStdString(str);
    ui->pushButton_4->setText(qstr);

    qstr = QString::fromStdString("A wild " + evilMatt->name + " approaches!");
    ui->mainDisplay->setText(qstr);

}

