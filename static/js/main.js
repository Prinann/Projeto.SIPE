document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const filtroStatus = document.getElementById('filtroStatus');
    const rows = document.querySelectorAll('#procuracoesTable tbody tr');

    // Função para filtrar linhas da tabela
    function filtrarProcuracoes() {
        const query = searchInput.value.toLowerCase();
        const statusSelecionado = filtroStatus.value;

        rows.forEach(row => {
            if (row.cells.length < 8) {
                row.style.display = '';
                return;
            }

            const numero = row.cells[0].textContent.toLowerCase();
            const outorgante = row.cells[1].textContent.toLowerCase();
            const outorgado = row.cells[2].textContent.toLowerCase();
            const statusRow = row.cells[5].textContent;

            const matchSearch = numero.includes(query) || outorgante.includes(query) || outorgado.includes(query);
            const matchStatus = !statusSelecionado || statusRow === statusSelecionado;

            row.style.display = (matchSearch && matchStatus) ? '' : 'none';
        });
    }

    // Eventos de input e select
    searchInput.addEventListener('input', filtrarProcuracoes);
    filtroStatus.addEventListener('change', filtrarProcuracoes);

    // Função para filtrar pelo clique em cards do dashboard
    window.filtrarPorStatus = (status) => {
        filtroStatus.value = status;
        filtrarProcuracoes();
    };

    // Scroll topo (se existir botão)
    const btnTopo = document.getElementById("btn-topo");
    if (btnTopo) {
        window.onscroll = () => {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                btnTopo.style.display = "block";
            } else {
                btnTopo.style.display = "none";
            }
        };

        window.topFunction = () => {
            document.body.scrollTop = 0;
            document.documentElement.scrollTop = 0;
        };
    }
});
