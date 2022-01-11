-- upgrade --
ALTER TABLE "category" ADD "name" VARCHAR(64) NOT NULL;
ALTER TABLE "document" ADD "subject" VARCHAR(128) NOT NULL;
ALTER TABLE "document" ADD "content" TEXT NOT NULL;
ALTER TABLE "document" ADD "category_id" INT NOT NULL;
ALTER TABLE "document" ADD "author_id" INT NOT NULL;
ALTER TABLE "document" ADD CONSTRAINT "fk_document_member_05a8da42" FOREIGN KEY ("author_id") REFERENCES "member" ("id") ON DELETE CASCADE;
ALTER TABLE "document" ADD CONSTRAINT "fk_document_category_afb79c90" FOREIGN KEY ("category_id") REFERENCES "category" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "document" DROP CONSTRAINT "fk_document_category_afb79c90";
ALTER TABLE "document" DROP CONSTRAINT "fk_document_member_05a8da42";
ALTER TABLE "category" DROP COLUMN "name";
ALTER TABLE "document" DROP COLUMN "subject";
ALTER TABLE "document" DROP COLUMN "content";
ALTER TABLE "document" DROP COLUMN "category_id";
ALTER TABLE "document" DROP COLUMN "author_id";
