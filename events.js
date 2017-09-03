class Event {
    constructor() {
        this.handlers = new Set();
    }

    subscribe(fn) {
        this.handlers.add(fn)
    }

    unsubscribe(fn) {
        this.handlers.delete(fn)
    }

    emit(...args) {
        this.handlers.forEach(fn => fn(...args))
    }
}

const event = new Event()
event.subscribe(() => 'hello')
event.subscribe(() => 'world')
event.subscribe(() => 'what is this')
event.unsubscribe()
event.emit()
