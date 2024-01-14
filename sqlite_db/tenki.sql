-- テーブルの作成
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

-- データの挿入
INSERT INTO users (name, age) VALUES ('John Doe', 25);
INSERT INTO users (name, age) VALUES ('Jane Smith', 30);

-- データの取得
SELECT * FROM users;

-- 条件に基づいたデータの取得
SELECT * FROM users WHERE age > 25;

-- データの更新
UPDATE users SET age = 26 WHERE name = 'John Doe';

-- データの削除
DELETE FROM users WHERE name = 'Jane Smith';