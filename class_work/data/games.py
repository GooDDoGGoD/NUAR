import sqlalchemy

from .db_session import SqlAlchemyBase


class Games(SqlAlchemyBase):
    __tablename__ = 'games'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    is_started = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    id_player_1 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, unique=True)
    id_player_2 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, unique=True)
    id_player_3 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, unique=True)

    status_1 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=1)
    status_2 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=1)
    status_3 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=1)

    def __repr__(self):
        return f'<Game> {self.id}'

    def add(self, id, n):
        if id not in [self.id_player_1, self.id_player_2, self.id_player_3]:
            if None == [self.id_player_1, self.id_player_2, self.id_player_3][n]:
                if n == 0:
                    self.id_player_1 = id
                elif n == 1:
                    self.id_player_2 = id
                elif n == 2:
                    self.id_player_3 = id

    def delete(self, id, n):
        if id == [self.id_player_1, self.id_player_2, self.id_player_3][n]:
            if n == 0:
                self.id_player_1 = None
            elif n == 1:
                self.id_player_2 = None
            elif n == 2:
                self.id_player_3 = None

    def defeat(self, id):
        for i in range(3):
            if id == [self.id_player_1, self.id_player_2, self.id_player_3][i]:
                [self.status_1, self.status_2, self.status_3][i] = 0

    def start(self):
        flag = True
        for x in [self.id_player_1, self.id_player_2, self.id_player_3]:
            if None == x:
                flag = False
                break
        self.is_started = flag
        self.is_finished = not flag
        return [self.id_player_1, self.id_player_2, self.id_player_3]

    def finish(self):
        if sum([self.status_1, self.status_2, self.status_3]) == 1:
            self.is_started = False
            self.is_finished = True
            for i in range(3):
                if [self.status_1, self.status_2, self.status_3][i] == 1:
                    id = [self.id_player_1, self.id_player_2, self.id_player_3][i]
                    break
            self.id_player_1, self.id_player_2, self.id_player_3 = None, None, None
            self.status_1, self.status_2, self.status_3 = 1, 1, 1
            return id