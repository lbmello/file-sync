"""Inicializador do pacote data."""

from .Time import Time
from .Config import Config
from .Host import Host as read_Host
from .Domain import Domain

from .write import Host as write_Host


# Variaveis globais de data
_nodes_ = None
_sync_levels_ = None
_times_ = None
_global_config_ = None
_share_config_ = None
_domain_ = None


def main():
    d_host = read_Host()
    d_time = Time()
    d_config = Config()
    d_domain = Domain()

    # TODO: Adicionar fechamento dos arquivos apos leitura

    global _nodes_
    _nodes_ = d_host.get_nodes()

    global _sync_levels_
    _sync_levels_ = d_host.get_sync_level()

    global _times_
    _times_ = d_time.get_times()

    global _global_config_
    _global_config_ = d_config.get_global_config()

    global _share_config_
    _share_config_ = d_config.get_share_config()

    global _domain_
    _domain_ = d_domain.get_domain()


main()