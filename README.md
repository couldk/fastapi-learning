# FastAPI Enterprise Learning

以实战项目驱动的 FastAPI 企业级后端开发学习仓库。

## 项目目标

通过开发一个订单管理系统，逐步学习：

- FastAPI 与 Pydantic v2
- 异步 SQLAlchemy 2.x
- PostgreSQL 与 Alembic
- JWT 与 RBAC
- Redis 缓存和限流
- Celery 消息任务
- Pytest 自动化测试
- Docker 部署
- 性能测试与监控

## 学习进度

- [ ] 阶段一：商品单表 CRUD
- [ ] 阶段二：PostgreSQL 与异步 ORM
- [ ] 阶段三：JWT 登录和 RBAC 权限
- [ ] 阶段四：订单、库存与事务
- [ ] 阶段五：Redis 缓存、限流和幂等
- [ ] 阶段六：Celery 异步任务
- [ ] 阶段七：Pytest 测试体系
- [ ] 阶段八：Docker Compose 部署
- [ ] 阶段九：异步服务聚合
- [ ] 阶段十：压测、日志与监控

## 当前实现

当前阶段：FastAPI 基础与商品 CRUD。

## 本地运行

```bash
python -m venv .venv
pip install -r requirements.txt
uvicorn app.main:app --reload
