from sanic import Sanic
from apps.example.blueprint import stats_bp
from configs import apps_configs

app = Sanic(__name__)
app.blueprint(stats_bp)

if __name__ == '__main__':
    app.run(host=apps_configs.host, port=apps_configs.port, workers=apps_configs.num_workers)
