DROP DATABASE hidden_monkey;
CREATE DATABASE hidden_monkey;
USE hidden_monkey;
CREATE TABLE video_list(
  video_id INT NOT NULL AUTO_INCREMENT,
  video_url TEXT,
  PRIMARY KEY (video_id)
);
CREATE TABLE video_stats(
  id INT AUTO_INCREMENT,
  video_id INT,
  video_views INT,
  time_collected DECIMAL(13,3),
  PRIMARY KEY (id),
  FOREIGN KEY (video_id)
    REFERENCES video_list(video_id)
);
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=k84FMc1GF8M');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=1b17ggwkR60');