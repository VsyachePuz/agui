import os, sys, argparse
path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(path, '..')))

import agui

#guis = [agui.APP.GTK, agui.APP.PYSIDE] #Doesn't seem to work, need to set the manually for now
#guis = [agui.APP.GTK]
guis = [agui.APP.PYSIDE]
#filenames = ['test_gtk.ui', 'test_qt.ui']
#filenames = ['test_gtk.ui']
filenames = ['test_qt.ui']

def test_gui():
    index = 0
    for gui in guis:
        window = setup_gui(gui, filenames[index])

        yield (button, window)
        yield (label, window)
        yield (checkbox, window)
        yield (combobox, window)
        yield (lineedit, window)
        yield (slider, window)
        yield (spinbox, window)
        yield (textarea, window)
        yield (treeview, window)

        close()

        index += 1

def setup_gui(gui, filename):
    reload(agui)
    agui.APP = agui.App()
    agui.APP.gui = gui

    from agui.widgets import Window
    return Window('test_window', os.path.join(path, filename))

def button(window):
    assert (window.widgets.test_button.text == 'button'), 'Button text should equal "button"'
    window.widgets.test_button.text = 'changed button'
    assert (window.widgets.test_button.text == 'changed button'), 'Button text should equal "changed button"'

def label(window):
    assert (window.widgets.test_label.text == 'label'), 'Label text should equal "label"'
    window.widgets.test_label.text = 'changed label'
    assert (window.widgets.test_label.text == 'changed label'), 'Label text should equal "changed label"'

def checkbox(window):
    assert (not window.widgets.test_checkbox.checked), 'Checkbox should not be checked'
    window.widgets.test_checkbox.checked = True
    assert (window.widgets.test_checkbox.checked), 'Checkbox should be checked'

def combobox(window):
    assert (len(window.widgets.test_combobox.items) == 0), 'Combobox should be empty'
    window.widgets.test_combobox.items = ['test1', 'test2']
    assert (len(window.widgets.test_combobox.items) == 2), 'Combobox should have 2 items'
    window.widgets.test_combobox.append('test3')
    assert (len(window.widgets.test_combobox.items) == 3), 'Combobox should have 3 items'
    window.widgets.test_combobox.selected = 1
    assert (window.widgets.test_combobox.selected == 1), 'Combobox should have 1 selected'
    assert (window.widgets.test_combobox.selected_text == 'test2'), 'Combobox should have "test2" as the selected test'

def lineedit(window):
    assert (window.widgets.test_lineedit.text == ''), 'Line edit should be empty'
    window.widgets.test_lineedit.text = 'asdf'
    assert (window.widgets.test_lineedit.text == 'asdf'), 'Line edit should be "asdf"'

def slider(window):
    assert (window.widgets.test_slider.value == 0), 'Slider value should be 0'
    window.widgets.test_slider.value = 5
    assert (window.widgets.test_slider.value == 5), 'Slider value should be 5'

def spinbox(window):
    assert (window.widgets.test_spinbox.value == 0), 'Spinbox value should be 0'
    window.widgets.test_spinbox.value = 5
    assert (window.widgets.test_spinbox.value == 5), 'Spinbox value should be 5'

def textarea(window):
    assert (window.widgets.test_textarea.text == ''), 'Text area should be empty'
    window.widgets.test_textarea.text = 'asdf'
    assert (window.widgets.test_textarea.text == 'asdf'), 'Text area should be "asdf"'

def treeview(window): #TODO: assert something in here
    window.widgets.test_treeview.add_row(0, ['a', 'b', 'c'], 'tooltip1', '#AAAAAA')
    window.widgets.test_treeview.add_row(1, ['d', 'e', 'f'], 'tooltip2', '#FFFFFF')


#slots
def close():
    agui.APP.quit()

def button_slot():
    print 'slot: button'

def checkbox_slot(checked):
    print 'slot: checkbox'
    print checked

def combobox_slot(index):
    print 'slot: combobox'
    print index

def lineedit_slot(text):
    print 'slot: lineedit'
    print text

def slider_slot(value):
    print 'slot: slider'
    print value

def spinbox_slot(value):
    print 'slot: spinbox'
    print value

def textarea_slot(text):
    print 'slot: textarea'
    print text

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--gtk', action='store_true', default=False)
    parser.add_argument('--pyside', action='store_true', default=False)
    args = parser.parse_args()

    window = None
    if args.gtk:
        window = setup_gui(agui.APP.GTK, 'test_gtk.ui')
    elif args.pyside:
        window = setup_gui(agui.APP.PYSIDE, 'test_qt.ui')
    else:
        raise RuntimeError('no gui specified')

    #signals
    window.closed.connect(close)
    window.widgets.test_button.pressed.connect(button_slot)
    window.widgets.test_checkbox.changed.connect(checkbox_slot)
    window.widgets.test_combobox.changed.connect(combobox_slot)
    window.widgets.test_lineedit.changed.connect(lineedit_slot)
    window.widgets.test_slider.changed.connect(slider_slot)
    window.widgets.test_spinbox.changed.connect(spinbox_slot)
    window.widgets.test_textarea.changed.connect(textarea_slot)

    treeview(window)

    window.show()
    agui.APP.run()

if __name__ == '__main__':
    main()
