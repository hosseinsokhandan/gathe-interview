-- upgrade --
ALTER TABLE "documentpermission" DROP CONSTRAINT "fk_document_member_d41f72ee";
ALTER TABLE "categorypermission" DROP CONSTRAINT "fk_category_member_e69e62b0";
ALTER TABLE "categorypermission" RENAME COLUMN "member_id_id" TO "member_id";
ALTER TABLE "documentpermission" RENAME COLUMN "member_id_id" TO "member_id";
ALTER TABLE "categorypermission" ADD CONSTRAINT "fk_category_member_a553ddb4" FOREIGN KEY ("member_id") REFERENCES "member" ("id") ON DELETE CASCADE;
ALTER TABLE "documentpermission" ADD CONSTRAINT "fk_document_member_cc87e133" FOREIGN KEY ("member_id") REFERENCES "member" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "documentpermission" DROP CONSTRAINT "fk_document_member_cc87e133";
ALTER TABLE "categorypermission" DROP CONSTRAINT "fk_category_member_a553ddb4";
ALTER TABLE "categorypermission" RENAME COLUMN "member_id" TO "member_id_id";
ALTER TABLE "documentpermission" RENAME COLUMN "member_id" TO "member_id_id";
ALTER TABLE "categorypermission" ADD CONSTRAINT "fk_category_member_e69e62b0" FOREIGN KEY ("member_id_id") REFERENCES "member" ("id") ON DELETE CASCADE;
ALTER TABLE "documentpermission" ADD CONSTRAINT "fk_document_member_d41f72ee" FOREIGN KEY ("member_id_id") REFERENCES "member" ("id") ON DELETE CASCADE;
