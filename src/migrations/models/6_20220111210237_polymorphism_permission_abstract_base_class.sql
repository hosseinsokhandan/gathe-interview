-- upgrade --
CREATE TABLE IF NOT EXISTS "permission" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "can_create" BOOL NOT NULL  DEFAULT False,
    "can_read" BOOL NOT NULL  DEFAULT False,
    "can_update" BOOL NOT NULL  DEFAULT False,
    "can_delete" BOOL NOT NULL  DEFAULT False,
    "member_id" INT NOT NULL REFERENCES "member" ("id") ON DELETE CASCADE
);
-- downgrade --
DROP TABLE IF EXISTS "permission";
