-- upgrade --
ALTER TABLE "documentpermission" ADD "can_create" BOOL NOT NULL  DEFAULT False;
-- downgrade --
ALTER TABLE "documentpermission" DROP COLUMN "can_create";
