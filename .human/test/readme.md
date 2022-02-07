# Development & testing

```bash
docker-compose --file testing-docker-compose.yml build arch-test && docker-compose --file testing-docker-compose.yml run --rm --name arch-test-dev --entrypoint /bin/zsh arch-test
```