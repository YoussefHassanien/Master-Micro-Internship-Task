import pytest
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from FunctionsPlotter import Ui_App

@pytest.fixture
def app_and_ui(qtbot):
    """Fixture to initialize the application and return the main window and UI object."""
    main_window = QWidget()
    ui = Ui_App()
    ui.setupUi(main_window)
    qtbot.addWidget(main_window)
    main_window.show()
    return main_window, ui

def test_invalid_function(app_and_ui, qtbot):
    """Test handling of invalid function input."""
    main_window, ui = app_and_ui
    ui.functionOneTextEdit.setPlainText("x**2 + y")
    ui.functionTwoTextEdit.setPlainText("2*x + 1")

    qtbot.mouseClick(ui.plotButton, Qt.LeftButton)

    assert not ui.functionOneErrorLabel.isHidden()
    assert "Undefined name 'y'" in ui.functionOneErrorLabel.text()

def test_empty_function(app_and_ui, qtbot):
    """Test handling of empty function input."""
    main_window, ui = app_and_ui
    ui.functionOneTextEdit.setPlainText("")
    ui.functionTwoTextEdit.setPlainText("2*x + 1")

    qtbot.mouseClick(ui.plotButton, Qt.LeftButton)

    assert not ui.functionOneErrorLabel.isHidden()
    assert "Function cannot be empty." in ui.functionOneErrorLabel.text()

def test_no_solution(app_and_ui, qtbot):
    """Test handling of functions that do not intersect."""
    main_window, ui = app_and_ui
    ui.functionOneTextEdit.setPlainText("x**2")
    ui.functionTwoTextEdit.setPlainText("-x**2 - 1")

    qtbot.mouseClick(ui.plotButton, Qt.LeftButton)

    assert not ui.solutionLabel.isHidden()
    assert "No solutions found." in ui.solutionLabel.text()

def test_math_domain_error(app_and_ui, qtbot):
    """Test handling of math domain errors."""
    main_window, ui = app_and_ui
    ui.functionOneTextEdit.setPlainText("sqrt(-1)*x")
    ui.functionTwoTextEdit.setPlainText("x")

    qtbot.mouseClick(ui.plotButton, Qt.LeftButton)

    assert not ui.functionOneErrorLabel.isHidden()
    assert "Math domain error" in ui.functionOneErrorLabel.text()

def test_syntax_error(app_and_ui, qtbot):
    """Test handling of syntax errors."""
    main_window, ui = app_and_ui
    ui.functionOneTextEdit.setPlainText("x**2 +")
    ui.functionTwoTextEdit.setPlainText("2*x + 1")

    qtbot.mouseClick(ui.plotButton, Qt.LeftButton)

    assert not ui.functionOneErrorLabel.isHidden()
    assert "Syntax error" in ui.functionOneErrorLabel.text()

def test_division_by_zero(app_and_ui, qtbot):
    """Test handling of division by zero."""
    main_window, ui = app_and_ui
    ui.functionOneTextEdit.setPlainText("x/0")
    ui.functionTwoTextEdit.setPlainText("2*x + 1")

    qtbot.mouseClick(ui.plotButton, Qt.LeftButton)

    assert not ui.functionOneErrorLabel.isHidden()
    assert "Division by zero" in ui.functionOneErrorLabel.text()

def test_multiple_roots(app_and_ui, qtbot):
    """Test handling of functions with multiple intersection points."""
    main_window, ui = app_and_ui
    ui.functionOneTextEdit.setPlainText("x**2 - 4")
    ui.functionTwoTextEdit.setPlainText("x")

    qtbot.mouseClick(ui.plotButton, Qt.LeftButton)

    assert not ui.solutionLabel.isHidden()
    assert "Solutions found at:" in ui.solutionLabel.text()
    assert "(-1.56, -1.56)" in ui.solutionLabel.text()
    assert "(2.56, 2.56)" in ui.solutionLabel.text()

def test_plot_numbers(app_and_ui, qtbot):
    """Test handling of plotting numbers."""
    main_window, ui = app_and_ui
    ui.functionOneTextEdit.setPlainText("3")
    ui.functionTwoTextEdit.setPlainText("x")

    qtbot.mouseClick(ui.plotButton, Qt.LeftButton)

    assert not ui.functionOneErrorLabel.isHidden()
    assert "An error occurred. Please check your function's syntax and variables." in ui.functionOneErrorLabel.text()    