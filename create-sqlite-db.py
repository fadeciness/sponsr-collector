import sqlite3 as sl

con = sl.connect('sponsrru-collector.db')

with con:
    # project_id = 000
    # level_id = 000
    # project_title = Project Title
    con.execute("""
        CREATE TABLE IF NOT EXISTS project_name (
            post_id INTEGER PRIMARY KEY,
            post_date VARCHAR(255),
            post_title VARCHAR(255),
            post_status VARCHAR(255),
            post_views INTEGER,
            post_access_type VARCHAR(255),
            post_access_value INTEGER,
            access_type VARCHAR(255),
            access_value INTEGER,
            level_price INTEGER,
            level_name VARCHAR(255),
            post_duration_podcast INTEGER,
            post_duration_text INTEGER,
            post_duration_video INTEGER,
            post_url VARCHAR(255)
        );
    """)

with con:
    con.execute("DELETE FROM project_name")

# sql = 'INSERT INTO edisclosureru (shortname, ticker, inn, site_company_id) VALUES (?, ?, ?, ?)'
# data = [
#     ('ПАО "Газпром нефть"', "MOEX:SIBN", "5504036333", "347"),
#     ('ПАО Сбербанк', "MOEX:SBER", "7707083893", "3043")
# ]
# with con:
#     con.executemany(sql, data)
#
# with con:
#     print("Table 'edisclosureru'")
#     data = con.execute("SELECT * FROM edisclosureru")
#     for row in data:
#         print(row)
#
# # TABLE: history of articles
# with con:
#     con.execute("""
#         CREATE TABLE IF NOT EXISTS edisclosureru_history (
#             id INTEGER PRIMARY KEY,
#             publication_date VARCHAR(30) NOT NULL,
#             event_name VARCHAR(255) NOT NULL,
#             event_url VARCHAR(255) NOT NULL,
#             shortname VARCHAR(255) NOT NULL,
#             site_company_id VARCHAR(255) NOT NULL,
#             is_notification_send INTEGER DEFAULT 0 NOT NULL,
#             FOREIGN KEY(shortname) REFERENCES edisclosureru(shortname),
#             FOREIGN KEY(site_company_id) REFERENCES edisclosureru(site_company_id)
#         );
#     """)
#
# with con:
#     con.execute("DELETE FROM edisclosureru_history")
#
# with con:
#     print("Table 'edisclosureru_history'")
#     data = con.execute("SELECT * FROM edisclosureru_history")
#     for row in data:
#         print(row)
#
# # TEMPORARY TABLE: tmp history of articles
# with con:
#     con.execute("""
#         CREATE TABLE IF NOT EXISTS tmp_edisclosureru_history (
#             publication_date VARCHAR(30) NOT NULL,
#             event_name VARCHAR(255) NOT NULL,
#             event_url VARCHAR(255) NOT NULL,
#             shortname VARCHAR(255) NOT NULL,
#             site_company_id VARCHAR(255) NOT NULL,
#             FOREIGN KEY(shortname) REFERENCES edisclosureru(shortname),
#             FOREIGN KEY(site_company_id) REFERENCES edisclosureru(site_company_id)
#         );
#     """)
#
# with con:
#     con.execute("DELETE FROM tmp_edisclosureru_history")
#
# with con:
#     print("Table 'tmp_edisclosureru_history'")
#     data = con.execute("SELECT * FROM tmp_edisclosureru_history")
#     for row in data:
#         print(row)
