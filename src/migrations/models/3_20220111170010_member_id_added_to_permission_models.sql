-- upgrade --
ALTER TABLE "categorypermission" ADD "member_id_id" INT NOT NULL;
ALTER TABLE "documentpermission" ADD "member_id_id" INT NOT NULL;
CREATE UNIQUE INDEX "uid_member_usernam_1d98a4" ON "member" ("username");
ALTER TABLE "categorypermission" ADD CONSTRAINT "fk_category_member_e69e62b0" FOREIGN KEY ("member_id_id") REFERENCES "member" ("id") ON DELETE CASCADE;
ALTER TABLE "documentpermission" ADD CONSTRAINT "fk_document_member_d41f72ee" FOREIGN KEY ("member_id_id") REFERENCES "member" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "documentpermission" DROP CONSTRAINT "fk_document_member_d41f72ee";
ALTER TABLE "categorypermission" DROP CONSTRAINT "fk_category_member_e69e62b0";
DROP INDEX "idx_member_usernam_1d98a4";
ALTER TABLE "categorypermission" DROP COLUMN "member_id_id";
ALTER TABLE "documentpermission" DROP COLUMN "member_id_id";
