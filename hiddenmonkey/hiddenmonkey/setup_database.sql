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
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=EU3d4PMBxkk');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=UBvVh_oG1O8');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=5-wXTJxQ350');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=0f1R265oU1A');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=urWQJTP8Nxc');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=qR4l1haDjvM');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=hxhpNHiBkeA');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=iopcfR1vI5I');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=1ISYT6EeUM0');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=ye8UpxnPzPE');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=O0wUwHIIg2A');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=tXmYdAm9Vjs');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=oPpYAFIYQBc');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=SobAPTAAX1s');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=2QxxD47NUaI');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=BrrgeZKvFEo');
INSERT INTO video_list(video_url) value('https://www.youtube.com/watch?v=DWnA-yXUmJI');