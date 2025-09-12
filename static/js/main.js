document.addEventListener('DOMContentLoaded', () => {
    // Busca
    const searchInput = document.getElementById('searchInput');
    const cards = document.querySelectorAll('#procuracoesList .card');

    searchInput.addEventListener('input', () => {
        const query = searchInput.value.toLowerCase();

        cards.forEach(card => {
            const outorgante = card.querySelector('.card-title').innerText.toLowerCase();
            const outorgado = card.querySelector('.card-text').innerText.toLowerCase();

            if (outorgante.includes(query) || outorgado.includes(query)) {
                card.closest('.col-lg-4').style.display = 'block';
            } else {
                card.closest('.col-lg-4').style.display = 'none';
            }
        });
    });

    // Filtro por status
    window.filtrarProcuracoes = () => {
        const statusSelecionado = document.getElementById('filtroStatus').value;

        cards.forEach(card => {
            const statusCard = card.dataset.status;

            if (!statusSelecionado || statusCard === statusSelecionado) {
                card.closest('.col-lg-4').style.display = 'block';
            } else {
                card.closest('.col-lg-4').style.display = 'none';
            }
        });
    };

    // Scroll topo
    const btnTopo = document.getElementById("btn-topo");
    window.onscroll = function() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            btnTopo.style.display = "block";
        } else {
            btnTopo.style.display = "none";
        }
    }

    window.topFunction = () => {
        document.body.scrollTop = 0; // Safari
        document.documentElement.scrollTop = 0; // Chrome, Firefox, IE e Opera
    }
});
