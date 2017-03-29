from django.conf.urls import include, url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='simpl/home.html'), name='simpl_home'),
    url(r'^/', include('simpl.games.urls.decision_urls')),
    url(r'^decisions/', include('simpl.games.urls.decision_urls')),
    url(r'^games/', include('simpl.games.urls.game_urls')),
    url(r'^periods/', include('simpl.games.urls.period_urls')),
    url(r'^phases/', include('simpl.games.urls.phase_urls')),
    url(r'^results/', include('simpl.games.urls.result_urls')),
    url(r'^roles/', include('simpl.games.urls.role_urls')),
    url(r'^runs/', include('simpl.games.urls.run_urls')),
    url(r'^scenarios/', include('simpl.games.urls.scenario_urls')),
    url(r'^worlds/', include('simpl.games.urls.world_urls')),
]
