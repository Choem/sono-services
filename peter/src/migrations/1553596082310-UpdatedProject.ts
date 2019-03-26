import {MigrationInterface, QueryRunner} from 'typeorm';

export class UpdatedProject1553596082310 implements MigrationInterface {

    public async up(queryRunner: QueryRunner): Promise<any> {
        await queryRunner.query('ALTER TABLE `project` ADD `description` varchar(255) NULL');
        await queryRunner.query('ALTER TABLE `project` ADD `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP');
    }

    public async down(queryRunner: QueryRunner): Promise<any> {
        await queryRunner.query('ALTER TABLE `project` DROP COLUMN `created_at`');
        await queryRunner.query('ALTER TABLE `project` DROP COLUMN `description`');
    }

}
