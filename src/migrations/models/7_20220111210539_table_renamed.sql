-- upgrade --
ALTER TABLE "categorypermission" RENAME TO "category_permission";
ALTER TABLE "documentpermission" RENAME TO "document_permission";
-- downgrade --
ALTER TABLE "category_permission" RENAME TO "categorypermission";
ALTER TABLE "document_permission" RENAME TO "documentpermission";
