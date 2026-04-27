from time import time
from app.models.block import Block


class Blockchain:
    """
    Blockchain logic layer
    """

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()

        new_block = Block(
            index=latest_block.index + 1,
            timestamp=time(),
            data=data,
            previous_hash=latest_block.hash
        )

        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True

    def get_chain(self):
        return [block.to_dict() for block in self.chain]