import {MigrationInterface, QueryRunner} from "typeorm";

export class RemovedDocumentId1551104516291 implements MigrationInterface {

    public async up(queryRunner: QueryRunner): Promise<any> {
        await queryRunner.query("ALTER TABLE `project_member` DROP FOREIGN KEY `FK_aaef76230abfcdf30adb15d0be8`");
        await queryRunner.query("ALTER TABLE `project` DROP COLUMN `document_id`");
        await queryRunner.query("ALTER TABLE `project_member` ADD CONSTRAINT `FK_aaef76230abfcdf30adb15d0be8` FOREIGN KEY (`project_id`) REFERENCES `project`(`id`) ON DELETE NO ACTION ON UPDATE NO ACTION");
    }

    public async down(queryRunner: QueryRunner): Promise<any> {
        await queryRunner.query("ALTER TABLE `project_member` DROP FOREIGN KEY `FK_aaef76230abfcdf30adb15d0be8`");
        await queryRunner.query("ALTER TABLE `project` ADD `document_id` varchar(255) NULL");
        await queryRunner.query("ALTER TABLE `project_member` ADD CONSTRAINT `FK_aaef76230abfcdf30adb15d0be8` FOREIGN KEY (`project_id`) REFERENCES `project`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT");
    }

}
