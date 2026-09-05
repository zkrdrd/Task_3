from random import choice
from string import ascii_lowercase

JS_DRAG_AND_DROP = """
function createEvent(typeOfEvent) {
    var event = document.createEvent("CustomEvent");
    event.initCustomEvent(typeOfEvent, true, true, null);
    event.dataTransfer = {
        data: {},
        setData: function (key, value) { this.data[key] = value; },
        getData: function (key) { return this.data[key]; }
    };
    return event;
}
function dispatchEvent(element, event, transferData) {
    if (transferData !== undefined) { event.dataTransfer = transferData; }
    if (element.dispatchEvent) { element.dispatchEvent(event); }
    else if (element.fireEvent) { element.fireEvent("on" + event.type, event); }
}
function simulateHTML5DragAndDrop(sourceElem, targetElem) {
    var dragStartEvent = createEvent('dragstart');
    dispatchEvent(sourceElem, dragStartEvent);
    var dragEnterEvent = createEvent('dragenter');
    dispatchEvent(targetElem, dragEnterEvent, dragStartEvent.dataTransfer);
    var dragOverEvent = createEvent('dragover');
    dispatchEvent(targetElem, dragOverEvent, dragStartEvent.dataTransfer);
    var dropEvent = createEvent('drop');
    dispatchEvent(targetElem, dropEvent, dragStartEvent.dataTransfer);
    var dragEndEvent = createEvent('dragend');
    dispatchEvent(sourceElem, dragEndEvent, dragStartEvent.dataTransfer);
}
simulateHTML5DragAndDrop(arguments[0], arguments[1]);
"""


def generate_random_string(length=10):
    """Генерирует случайную строку из строчных букв."""
    letters = ascii_lowercase
    return "".join(choice(letters) for _ in range(length))


def generate_unique_email():
    """Генерирует уникальный email."""
    return f"{generate_random_string()}@example.com"
