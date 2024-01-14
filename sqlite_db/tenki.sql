-- テーブルの作成
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

-- データの挿入
INSERT INTO users (name, age) VALUES ('John Doe', 25);
INSERT INTO users (name, age) VALUES ('Jane Smith', 30);
