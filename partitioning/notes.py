# Partitioning refers to splitting what is logically one large table into smaller physical pieces.
# Benefits: Query performance can be improved dramatically
# Bulk loads and deletes can be accomplished by adding or removing partitions,
# if the usage pattern is accounted for in the partitioning design.
# Dropping an individual partition using DROP TABLE,
# or doing ALTER TABLE DETACH PARTITION, is far faster than a bulk operation.
# These commands also entirely avoid the VACUUM overhead caused by a bulk DELETE.

# POSTGRES Support:
# Range partitioning: example created_at
# List partitioning: examples regions(US, EU, AP)
# Hash partitioning: Custom key "userId"

# Examples:
# CREATE TABLE orders (
#     id SERIAL,
#     customer_id INT,
#     order_date DATE
# ) PARTITION BY RANGE (order_date);
#
# CREATE TABLE orders_2023_01 PARTITION OF orders FOR VALUES FROM ('2023-01-01') TO ('2023-02-01');
# CREATE TABLE orders_2023_02 PARTITION OF orders FOR VALUES FROM ('2023-02-01') TO ('2023-03-01');

# HASH:
#CREATE TABLE users (
#     id SERIAL,
#     name TEXT,
#     email TEXT
# ) PARTITION BY HASH (id);
#
# CREATE TABLE users_partition_0 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 0);
# CREATE TABLE users_partition_1 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 1);
# CREATE TABLE users_partition_2 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 2);
# CREATE TABLE users_partition_3 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 3);

# LIST:
#-- Create the parent table with list partitioning
# CREATE TABLE users (
#     id SERIAL,
#     name TEXT,
#     email TEXT,
#     region TEXT
# ) PARTITION BY LIST (region);
#
# -- Create partitions for specific regions
# CREATE TABLE users_us PARTITION OF users FOR VALUES IN ('US');
# CREATE TABLE users_eu PARTITION OF users FOR VALUES IN ('EU');
# CREATE TABLE users_apac PARTITION OF users FOR VALUES IN ('APAC');
#
# -- Create a default partition for other regions
# CREATE TABLE users_other PARTITION OF users DEFAULT;


# NOTE: we need to create the tables separately for each partition with custom script i.e. like line 21 and 22

# regular tables can't be converted to partitioned tables but we can attach the partition to regular tables

# NOTE: Create index will automatically creates the index for partitions as well as per docs.
# Can a table without a primary key be partitioned? = >Yes, but it's not recommended
# as it can lead to data consistency and query optimization issues.

# skewed partition => data is un-uniformly present and query performance degrades

# Need to enable partition pruning to allow indexes to avoid all partition scans when where clause mentioned.

# Interesting video: https://www.youtube.com/watch?v=edQZauVU-ws&t=1s&ab_channel=JimmyAngelakos