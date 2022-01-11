-- upgrade --
ALTER TABLE "categorypermission" ADD "can_create" BOOL NOT NULL  DEFAULT False;
ALTER TABLE "categorypermission" ADD "can_delete" BOOL NOT NULL  DEFAULT False;
ALTER TABLE "categorypermission" ADD "category_id" INT NOT NULL;
ALTER TABLE "categorypermission" ADD "can_update" BOOL NOT NULL  DEFAULT False;
ALTER TABLE "categorypermission" ADD "can_read" BOOL NOT NULL  DEFAULT False;
ALTER TABLE "documentpermission" ADD "can_delete" BOOL NOT NULL  DEFAULT False;
ALTER TABLE "documentpermission" ADD "document_id" INT NOT NULL;
ALTER TABLE "documentpermission" ADD "can_update" BOOL NOT NULL  DEFAULT False;
ALTER TABLE "documentpermission" ADD "can_read" BOOL NOT NULL  DEFAULT False;
ALTER TABLE "categorypermission" ADD CONSTRAINT "fk_category_category_1e0c9809" FOREIGN KEY ("category_id") REFERENCES "category" ("id") ON DELETE CASCADE;
ALTER TABLE "documentpermission" ADD CONSTRAINT "fk_document_document_6902a983" FOREIGN KEY ("document_id") REFERENCES "document" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "documentpermission" DROP CONSTRAINT "fk_document_document_6902a983";
ALTER TABLE "categorypermission" DROP CONSTRAINT "fk_category_category_1e0c9809";
ALTER TABLE "categorypermission" DROP COLUMN "can_create";
ALTER TABLE "categorypermission" DROP COLUMN "can_delete";
ALTER TABLE "categorypermission" DROP COLUMN "category_id";
ALTER TABLE "categorypermission" DROP COLUMN "can_update";
ALTER TABLE "categorypermission" DROP COLUMN "can_read";
ALTER TABLE "documentpermission" DROP COLUMN "can_delete";
ALTER TABLE "documentpermission" DROP COLUMN "document_id";
ALTER TABLE "documentpermission" DROP COLUMN "can_update";
ALTER TABLE "documentpermission" DROP COLUMN "can_read";
