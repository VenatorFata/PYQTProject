import sys
import random
import sqlite3
import os

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtWidgets
from menu import Ui_MainWindow
from gameplay import Ui_Form as gameplay_UI
from tasks import Ui_Form as tasks_UI
from db_table import Ui_Form as table_UI


class DrillProjectMenu(QMainWindow, Ui_MainWindow):
    # Менюшка игры, первое окно что ты видишь
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # Кнопки
        self.startButton.setText('Начать игру')
        self.exitButton.clicked.connect(self.exit)
        self.startButton.clicked.connect(self.start_game)
        self.tableButton.clicked.connect(self.table_view)
        self.addButton.clicked.connect(self.add_player)
        self.selectButton.clicked.connect(self.select_player)
        self.nameLine.textChanged.connect(self.change_text)
        self.guideButton.clicked.connect(self.open_guide)
        # Переменные и надписи
        # Пояснительная записка и руководство по бурению.txt
        self.chosen_player_name = 'PlayerName'
        self.addUserName = 'PlayerName'
        self.errorLabel_text1 = self.errorLabel.text()
        self.errorLabel_text2 = 'Работник уже есть в системе!'
        self.errorLabel.setText('')
        self.widget = None

    def change_text(self):
        self.addUserName = self.nameLine.text()
        
    def open_guide(self):
        os.startfile(r'Пояснительная записка и руководство по бурению.txt')

    def add_player(self):
        if DBTable().add_player(username=self.addUserName) == 1:
            self.errorLabel.setText(self.errorLabel_text2)

    def select_player(self):
        self.chosen_player_name = DBTable().select_player(username=self.nameLine.text())
        if self.chosen_player_name is None:
            self.errorLabel.setText(self.errorLabel_text1)
        else:
            self.errorLabel.setText('Работник был выбран!')

    def exit(self):
        # Выход из меню и игры
        self.close()

    def start_game(self):
        # Начало игры (переход на виджет с задачами)
        self.widget = TaskChoose(self.chosen_player_name)
        self.widget.show()
        self.hide()

    def table_view(self):
        self.widget = DBTable()
        self.widget.show()
        self.hide()


class TaskChoose(QWidget, tasks_UI):
    def __init__(self, player_name):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # Переменные
        self.chosen_player_name = player_name
        self.menuWidget = DrillProjectMenu()
        # Генерация заданий
        self.task1_depth, self.task1_time = random.randrange(90, 180), random.randrange(135, 240)
        self.task2_depth, self.task2_time = random.randrange(100, 200), random.randrange(120, 180)
        self.task3_depth, self.task3_time = random.randrange(120, 240), random.randrange(105, 150)
        self.task1_label.setText(f'Глубина - {str(self.task1_depth)} м \n' +
                                 f'Время - {str(self.task1_time)} сек')
        self.task2_label.setText(f'Глубина - {str(self.task2_depth)} м \n' +
                                 f'Время - {str(self.task2_time)} сек')
        self.task3_label.setText(f'Глубина - {str(self.task3_depth)} м \n' +
                                 f'Время - {str(self.task3_time)} сек')
        # Выбор заданий и переход к игре
        self.task1_button.pressed.connect(self.gameplay_launch)
        self.task2_button.pressed.connect(self.gameplay_launch)
        self.task3_button.pressed.connect(self.gameplay_launch)
        self.taskLabel.setText(self.taskLabel.text() + self.chosen_player_name)
        # Иконка на кнопку
        self.returnButton.setIcon(QIcon('undo-1024.webp'))
        # Кнопка возврата в меню
        self.returnButton.clicked.connect(self.return_to_menu)

        self.widget = None

    def gameplay_launch(self):
        if self.sender().text()[-1] == '1':
            self.widget = Gameplay(self.task1_depth, self.task1_time, self.chosen_player_name)
        elif self.sender().text()[-1] == '2':
            self.widget = Gameplay(self.task2_depth, self.task2_time, self.chosen_player_name)
        elif self.sender().text()[-1] == '3':
            self.widget = Gameplay(self.task3_depth, self.task3_time, self.chosen_player_name)
        self.widget.show()
        self.hide()

    def show_yourself(self):
        self.show()

    def return_to_menu(self):
        self.close()

    def closeEvent(self, event):
        super().closeEvent(event)
        self.menuWidget.show()
        event.accept()


class Gameplay(QWidget, gameplay_UI):

    def __init__(self, depth, time, player_name):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # Кнопка для начала игры
        self.startButton.setText('Начать бурение')
        # Глубина бурения
        self.req_depth = depth
        self.cur_depth = 0
        self.progressBar.setMaximum(self.req_depth)
        # Об/мин бура
        self.req_RPM = random.randrange(20, 120, 5)
        self.cur_RPM = self.RPMbox.value()
        self.drillRPMText = self.drillLabel_3.text()
        self.drillLabel_3.setText(self.drillRPMText + str(self.req_RPM))
        # Бурильная жидкость
        self.cur_fluid = float(random.randrange(0, 30))
        self.fluid_drain_speed = float(((self.req_depth - self.req_depth % 2) // 5) / 100 + 1)
        self.fluidBar.setValue(int(self.cur_fluid))
        self.fluidRefillButton.clicked.connect(self.fluid_refill)
        self.timeToRechargeFluid = 0
        self.fluidRefillText = self.fluidRefillButton.text()
        # Долото бура
        self.drillLabel.setText(self.drillLabel.text() + random.choice(['Т', 'С', 'М']))
        if self.drillLabel.text()[-1] == 'Т':
            self.req_drillHead = 'Heavy'
        elif self.drillLabel.text()[-1] == 'С':
            self.req_drillHead = 'Medium'
        else:
            self.req_drillHead = 'Light'
        self.cur_drillHead = 'Heavy'
        self.chosen_drillHead = self.cur_drillHead
        self.drillLabel_2.setText(self.drillLabel_2.text() + 'Т')
        self.comboDrillHead.currentTextChanged.connect(self.change_state_of_button)
        self.acceptDrillHead.clicked.connect(self.accept_current_drill_head)
        self.changeDrillHead.clicked.connect(self.change_current_drill_head)
        self.buttonText_1 = self.changeDrillHead.text()
        self.buttonText_2 = self.acceptDrillHead.text()
        # Всячина по долотам
        self.waitTime = 0
        self.heavyRepairWaitTime = 0
        self.mediumRepairWaitTime = 0
        self.lightRepairWaitTime = 0
        self.changeDrillHead.setEnabled(False)
        # Генерация прочности долот бура
        self.heavyStatus.setValue(random.randrange(1, 30))
        self.mediumStatus.setValue(random.randrange(1, 20))
        self.lightStatus.setValue(random.randrange(1, 10))
        # Всякая всячина
        self.chosen_player_name = player_name
        self.time = time
        self.rem_time = self.time
        self.drillHead_change_req_time = random.randrange(15, 25)
        self.RPM_change_req_time = random.randrange(10, 30)
        self.depthLabel.setText(f'Требуемая глубина - {self.req_depth} м')
        self.timeLCD.display(self.time)
        self.endButton.clicked.connect(self.end_game)
        self.startButton.clicked.connect(self.start_game)
        self.repairButtonGroup.buttonClicked.connect(self.repair_drill_head)
        self.taskWidget = TaskChoose(self.chosen_player_name)
        self.label.setText(self.label.text() + self.chosen_player_name)
        # Настройка таймера до конца игры
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.game_end)
        # Настройка таймера на обновление времени
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_time)
        self.update_timer.timeout.connect(self.game_process)

    def start_game(self):
        self.timer.start(self.time * 1000)
        self.update_timer.start(1000)
        self.startButton.setEnabled(False)
        self.startButton.setText('Бурение началось')

    def change_state_of_button(self):
        self.acceptDrillHead.setEnabled(True)

    def accept_current_drill_head(self):
        if self.changeDrillHead.text() != self.buttonText_1:
            self.acceptDrillHead.setText('Error!')
        else:
            if self.comboDrillHead.currentText() == 'Т':
                self.cur_drillHead = 'Heavy'
                self.waitTime = random.randrange(11, 19)
            elif self.comboDrillHead.currentText() == 'С':
                self.cur_drillHead = 'Medium'
                self.waitTime = random.randrange(8, 16)
            else:
                self.cur_drillHead = 'Light'
                self.waitTime = random.randrange(5, 13)
            self.changeDrillHead.setEnabled(True)
            self.acceptDrillHead.setEnabled(False)

    def change_current_drill_head(self):
        if self.changeDrillHead.isEnabled():
            self.changeDrillHead.setText(f'{self.waitTime}...')
            self.changeDrillHead.setEnabled(False)
            self.chosen_drillHead = self.cur_drillHead

    def repair_drill_head(self, button):  # Починка долота бура
        if button == self.heavyRepair and self.heavyRepairWaitTime == 0:
            self.heavyStatus.setValue(self.heavyStatus.maximum())
            self.heavyRepairWaitTime = 20
            self.heavyRepair.setText(f'{self.heavyRepairWaitTime}...')
            self.heavyRepair.setEnabled(False)
        if button == self.mediumRepair and self.mediumRepairWaitTime == 0:
            self.mediumStatus.setValue(self.mediumStatus.maximum())
            self.mediumRepairWaitTime = 15
            self.mediumRepair.setText(f'{self.mediumRepairWaitTime}...')
            self.mediumRepair.setEnabled(False)
        if button == self.lightRepair and self.lightRepairWaitTime == 0:
            self.lightStatus.setValue(self.lightStatus.maximum())
            self.lightRepairWaitTime = 10
            self.lightRepair.setText(f'{self.lightRepairWaitTime}...')
            self.lightRepair.setEnabled(False)

    def fluid_refill(self):
        self.cur_fluid = 20.0
        self.fluidRefillButton.setEnabled(False)
        self.fluidBar.setValue(self.fluidBar.maximum())
        self.timeToRechargeFluid = 15
        self.fluidRefillButton.setText(f'{self.timeToRechargeFluid}...')

    def game_end(self):
        self.timer.stop()
        self.game_ended = True
        if self.time != 0 and self.cur_depth == self.req_depth:
            DBTable().update_base(self.chosen_player_name, self.cur_depth, 1, 0)
        else:
            DBTable().update_base(self.chosen_player_name, self.cur_depth, 0, 1)

    def update_time(self):
        if self.rem_time > 0:
            self.rem_time -= 1
            self.timeLCD.display(self.rem_time)
        if self.waitTime > 0:
            self.waitTime -= 1
        if self.heavyRepairWaitTime > 0:
            self.heavyRepairWaitTime -= 1
        if self.mediumRepairWaitTime > 0:
            self.mediumRepairWaitTime -= 1
        if self.lightRepairWaitTime > 0:
            self.lightRepairWaitTime -= 1
        if self.timeToRechargeFluid > 0:
            self.timeToRechargeFluid -= 1

    def game_process(self):
        added_depth = 0
        repair_drill_text = 'Починить долото'
        if self.cur_depth == self.req_depth:
            self.game_end()
            self.timer.stop()
            self.update_timer.stop()
        self.cur_RPM = self.RPMbox.value()
        if self.chosen_drillHead == 'Heavy':
            cur_drill_status = self.heavyStatus.value()
        elif self.chosen_drillHead == 'Medium':
            cur_drill_status = self.mediumStatus.value()
        else:
            cur_drill_status = self.lightStatus.value()
        # Рандомный выбор об/мин
        if self.rem_time % self.RPM_change_req_time == 0:
            self.req_RPM = random.randrange(20, 120, 5)
            self.drillLabel_3.setText(self.drillRPMText + str(self.req_RPM))
        # Рандомный выбор требуемого долота
        if self.rem_time % self.drillHead_change_req_time == 0:
            self.drillLabel.setText(self.drillLabel.text()[:-1] + random.choice(['Т', 'С', 'М']))
            if self.drillLabel.text()[-1] == 'Т':
                self.req_drillHead = 'Heavy'
            elif self.drillLabel.text()[-1] == 'С':
                self.req_drillHead = 'Medium'
            else:
                self.req_drillHead = 'Light'
        # Изменение надписи о текущем долоте
        if self.chosen_drillHead == 'Heavy':
            self.drillLabel_2.setText(self.drillLabel_2.text()[:-1] + 'Т')
        elif self.chosen_drillHead == 'Medium':
            self.drillLabel_2.setText(self.drillLabel_2.text()[:-1] + 'С')
        else:
            self.drillLabel_2.setText(self.drillLabel_2.text()[:-1] + 'М')
        # Трата бурильной жидкости
        try:
            if self.cur_fluid > 0.0:
                self.cur_fluid -= self.fluid_drain_speed
                if self.fluidBar.value() < self.fluid_drain_speed:
                    self.fluidBar.setValue(0)
                else:
                    self.fluidBar.setValue(int(self.cur_fluid))
            else:
                if self.chosen_drillHead == 'Heavy':
                    self.heavyStatus.setValue(self.heavyStatus.value() - 1)
                elif self.chosen_drillHead == 'Medium':
                    self.mediumStatus.setValue(self.mediumStatus.value() - 1)
                else:
                    self.lightStatus.setValue(self.lightStatus.value() - 1)
            if self.timeToRechargeFluid == 0:
                self.fluidRefillButton.setEnabled(True)
                self.fluidRefillButton.setText(self.fluidRefillText)
            else:
                self.fluidRefillButton.setText(f'{self.timeToRechargeFluid}...')
        except EnvironmentError as e:
            print(e)
        # Об/мин != требуемому Об/Мин
        if self.cur_RPM != self.req_RPM:
            if self.chosen_drillHead == 'Heavy':
                self.heavyStatus.setValue(self.heavyStatus.value() - 1)
            elif self.chosen_drillHead == 'Medium':
                self.mediumStatus.setValue(self.mediumStatus.value() - 1)
            else:
                self.lightStatus.setValue(self.lightStatus.value() - 1)
        else:
            added_depth += 1
        # Текущее долото не соответствует требуемому долоту
        if self.chosen_drillHead != self.req_drillHead:
            if self.chosen_drillHead == 'Heavy':
                self.heavyStatus.setValue(self.heavyStatus.value() - 1)
            elif self.chosen_drillHead == 'Medium':
                self.mediumStatus.setValue(self.mediumStatus.value() - 1)
            else:
                self.lightStatus.setValue(self.lightStatus.value() - 1)
            added_depth = 0
        if cur_drill_status == 0:
            added_depth = 0
        if self.chosen_drillHead == self.req_drillHead and cur_drill_status != 0:
            added_depth += 1
        # Починка буров - кнопки
        if self.heavyRepairWaitTime == 0:  # Тяжёлое долото
            self.heavyRepair.setText(repair_drill_text)
            self.heavyRepair.setEnabled(True)
        else:
            self.heavyRepair.setText(f'{self.heavyRepairWaitTime}...')
        if self.mediumRepairWaitTime == 0:  # Среднее долото
            self.mediumRepair.setText(repair_drill_text)
            self.mediumRepair.setEnabled(True)
        else:
            self.mediumRepair.setText(f'{self.mediumRepairWaitTime}...')
        if self.lightRepairWaitTime == 0:  # Лёгкое долото
            self.lightRepair.setText(repair_drill_text)
            self.lightRepair.setEnabled(True)
        else:
            self.lightRepair.setText(f'{self.lightRepairWaitTime}...')
        # Смена буров - включение кнопки
        if self.waitTime == 0:
            self.changeDrillHead.setText(self.buttonText_1)
            self.changeDrillHead.setDisabled(True)
        elif self.waitTime != 0 and not self.changeDrillHead.isEnabled():
            self.changeDrillHead.setText(f'{self.waitTime}...')
        self.acceptDrillHead.setText(self.buttonText_2)
        self.cur_depth += added_depth
        if self.cur_depth + added_depth > self.req_depth:
            self.cur_depth = self.req_depth
            self.progressBar.setValue(self.cur_depth)
        else:
            self.progressBar.setValue(self.cur_depth)

    def end_game(self):
        self.close()

    def closeEvent(self, event):
        super().closeEvent(event)
        self.taskWidget.show()
        self.update_timer.stop()
        self.timer.stop()
        event.accept()


class DBTable(QWidget, table_UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.db_name = 'players_db.db'
        self.returnButton.setIcon(QIcon('undo-1024.webp'))
        self.returnButton.clicked.connect(self.return_to_menu)
        self.load_data()
        self.widget = None

    def load_data(self):
        # Подключение к базе данных
        connection = sqlite3.connect(self.db_name)
        cur = connection.cursor()
        cur.execute("""SELECT * FROM players_table""")
        column_names = [description[0] for description in cur.description]
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setHorizontalHeaderLabels(column_names)
        rows = cur.fetchall()
        self.tableWidget.setRowCount(len(rows))
        # Заполнение таблицы данными
        for row_index, row_data in enumerate(rows):
            for column_index, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(cell_data)))
        connection.close()

    def add_player(self, username):
        connection = sqlite3.connect(self.db_name)
        cur = connection.cursor()
        try:
            cur.execute("""INSERT INTO players_table (username, tasks_completed, tasks_failed, meters_drilled)
                        VALUES (?, ?, ?, ?)""", (username, 0, 0, 0))
            connection.commit()
        except sqlite3.IntegrityError:
            return 1
        finally:
            connection.close()

    def select_player(self, username):
        connection = sqlite3.connect(self.db_name)
        cur = connection.cursor()
        try:
            result = cur.execute(f"""SELECT username FROM players_table WHERE username=?""", (username,)).fetchone()
            if result is not None:
                return result[0]
            else:
                return None
        except sqlite3.Error as e:
            print(e)
            return 2
        finally:
            connection.close()

    def return_to_menu(self):
        self.widget = DrillProjectMenu()
        self.widget.show()
        self.close()

    def update_base(self, username, depth, task_success, task_fail):
        connection = sqlite3.connect(self.db_name)
        cur = connection.cursor()
        try:
            results = cur.execute("""SELECT tasks_completed, 
                                  tasks_failed, meters_drilled FROM players_table WHERE username = ?""",
                                  (username,)).fetchall()
            success = task_success + results[0][0]
            fail = task_fail + results[0][1]
            depth += results[0][2]
            cur.execute("""UPDATE players_table SET meters_drilled = ?, tasks_completed = ?,
                        tasks_failed = ? WHERE username = ?""",
                        (depth, success, fail, username))
            connection.commit()
        except sqlite3.Error as e:
            print(e)
            return 3
        finally:
            connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrillProjectMenu()
    ex.show()
    sys.exit(app.exec())