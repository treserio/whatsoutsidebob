#!/bin/bash
sudo cat object_import.sql | mysql -uroot -proot --local-infile=1
