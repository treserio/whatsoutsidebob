ALTER TABLE subjects MODIFY EPISODE VARCHAR(30);
ALTER TABLE colors MODIFY EPISODE VARCHAR(30);
ALTER TABLE pic_info MODIFY episode_subjects VARCHAR(30);
ALTER TABLE pic_info MODIFY episode_colors VARCHAR(30);

ALTER TABLE subjects ADD PRIMARY KEY (EPISODE);
ALTER TABLE colors ADD PRIMARY KEY (EPISODE);

ALTER TABLE pic_info ADD FOREIGN KEY (episode_subjects) REFERENCES subjects(EPISODE) ON DELETE CASCADE;

ALTER TABLE pic_info ADD FOREIGN KEY (episode_colors) REFERENCES colors(EPISODE) ON DELETE CASCADE;
