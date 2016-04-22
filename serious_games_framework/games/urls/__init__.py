from django.conf.urls import include, url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='simpl/home.html'), name='simpl_home'),
    url(r'^/', include('serious_games_framework.games.urls.decision_urls')),
    url(r'^decisions/', include('serious_games_framework.games.urls.decision_urls')),
    url(r'^games/', include('serious_games_framework.games.urls.game_urls')),
    url(r'^periods/', include('serious_games_framework.games.urls.period_urls')),
    url(r'^phases/', include('serious_games_framework.games.urls.phase_urls')),
    url(r'^results/', include('serious_games_framework.games.urls.result_urls')),
    url(r'^roles/', include('serious_games_framework.games.urls.role_urls')),
    url(r'^rounds/', include('serious_games_framework.games.urls.round_urls')),
    url(r'^runs/', include('serious_games_framework.games.urls.run_urls')),
    url(r'^scenarios/', include('serious_games_framework.games.urls.scenario_urls')),
    url(r'^webhook_logs/', include('serious_games_framework.games.urls.webhook_log_urls')),
    url(r'^webhooks/', include('serious_games_framework.games.urls.webhook_urls')),
    url(r'^worlds/', include('serious_games_framework.games.urls.world_urls')),
]
