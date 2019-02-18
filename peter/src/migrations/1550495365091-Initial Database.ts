import {MigrationInterface, QueryRunner} from "typeorm";

export class InitialDatabase1550495365091 implements MigrationInterface {

    public async up(queryRunner: QueryRunner): Promise<any> {
        await queryRunner.query("CREATE TABLE `project` (`id` int NOT NULL AUTO_INCREMENT, `document_id` varchar(255) NULL, `user_id` int NOT NULL, `name` varchar(255) NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB");
        await queryRunner.query("CREATE TABLE `project_member` (`user_id` int NOT NULL, `project_id` int NOT NULL, PRIMARY KEY (`user_id`, `project_id`)) ENGINE=InnoDB");
        await queryRunner.query("ALTER TABLE `project_member` ADD CONSTRAINT `FK_aaef76230abfcdf30adb15d0be8` FOREIGN KEY (`project_id`) REFERENCES `project`(`id`)");
    }

    public async down(queryRunner: QueryRunner): Promise<any> {
        await queryRunner.query("ALTER TABLE `project_member` DROP FOREIGN KEY `FK_aaef76230abfcdf30adb15d0be8`");
        await queryRunner.query("DROP TABLE `project_member`");
        await queryRunner.query("DROP TABLE `project`");
    }

}
