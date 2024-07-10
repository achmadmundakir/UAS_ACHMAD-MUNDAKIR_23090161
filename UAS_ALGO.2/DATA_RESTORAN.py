# File: queue_restoran.py
class QueueRestoran:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Pesanan {item} telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            print(f"Pesanan {item} telah selesai diproses dan dihapus dari antrian.")
            return item
        else:
            print("Antrian kosong.")
            return None

    def is_empty(self):
        return len(self.items) == 0
