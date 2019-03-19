import {
  Body,
  Controller,
  Get,
  HttpStatus, Param,
  Post,
  Query,
} from '@nestjs/common';
import { ProjectService } from '../../services/project/project.service';
import { BaseController } from '../../../../common/baseController';
import { ProjectCreateDto } from '../../dtos/projectCreateDto';
import { ApiResponse, ApiOperation, ApiUseTags } from '@nestjs/swagger';
import { GrpcMethod } from '@nestjs/microservices';

@Controller()
@ApiUseTags('projects')
@ApiResponse({ status: HttpStatus.FORBIDDEN, description: 'Forbidden.' })
@ApiResponse({ status: HttpStatus.UNAUTHORIZED, description: 'Unauthorized.' })
export class ProjectController extends BaseController {
  constructor(private readonly projectService: ProjectService) {
    super();
  }

  @Get()
  @ApiOperation({ title: 'Get all projects' })
  @ApiResponse({
    status: HttpStatus.OK,
  })
  public async all(
    @Query('size') pageSize: number,
    @Query('page') page: number,
  ) {
    const [ projects, total ] = await this.projectService.getAll(pageSize, page);
    return this.api(true, { data: {projects, total} });
  }

  @Post()
  @ApiOperation({ title: 'Create a new Project' })
  @ApiResponse({
    status: HttpStatus.CREATED,
    description: 'Project has been successfully created.',
  })
  @ApiResponse({
    status: HttpStatus.CONFLICT,
    description: 'Project already exists.',
  })
  public async create(@Body() userCreateDto: ProjectCreateDto) {
    await this.projectService.create(userCreateDto);
    return this.api(true, { label: 'project.create.success' });
  }

  @Get(':id')
  @ApiOperation({ title: 'Find a Project' })
  @ApiResponse({
    status: HttpStatus.OK,
    description: 'Project has been successfully returned.',
  })
  @ApiResponse({
    status: HttpStatus.NOT_FOUND,
    description: 'Project not found.',
  })
  public async find(@Param('id') id) {
    const project = await this.projectService.findById(id);
    return this.api(true, { data: project });
  }

  @GrpcMethod('ProjectService')
  async findOne(data: { id: number }) {
    return await this.projectService.findById(data.id);
  }

  @GrpcMethod('ProjectService')
  async findAll() {
    return { projects: (await this.projectService.getAll())[0] };
  }
}
