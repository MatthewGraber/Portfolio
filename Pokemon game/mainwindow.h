/*
 * Matthew Graber, Cameron Luzadder, Katherine Newman
 * Runs the GUI
 */

#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "creature.h"


QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

    Creature* realMatt;
    Creature* evilMatt;
    string *que;

    void run();
    void run(Creature player, Creature enemy);

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_4_clicked();

    void on_progressBar_valueChanged(int value);

    //void on_label_2_linkActivated(const QString &link);

private:
    Ui::MainWindow *ui;
    void initalizeFighter(Creature *fighter, QLabel *personalDisplay, QProgressBar *healthbar);
};
#endif // MAINWINDOW_H
