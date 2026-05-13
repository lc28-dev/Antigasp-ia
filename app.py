<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>L'Art de Bien Manger | Anti-Gaspi & Plaisir</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
    
    <style>
        /* Variables de couleurs */
        :root {
            --primary: #2d5a27; /* Vert forêt */
            --accent: #e67e22; /* Orange doux */
            --text: #2c3e50;
            --light: #f9f7f2;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            color: var(--text);
            line-height: 1.6;
            background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
            overflow-x: hidden;
        }

        /* Hero Section avec image floutée */
        .hero {
            position: relative;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            padding: 20px;
        }

        .hero-bg {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            /* Image de nourriture réelle en haute qualité */
            background: url('https://images.unsplash.com/photo-1490818387583-1baba5e638af?auto=format&fit=crop&q=80&w=1920');
            background-size: cover;
            background-position: center;
            filter: blur(4px) brightness(0.6); /* Flou + assombrissement */
            z-index: -1;
        }

        .hero-content h1 {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2.5rem, 8vw, 5rem);
            margin-bottom: 20px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        }

        .hero-content p {
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto 30px;
            font-weight: 300;
        }

        .btn {
            display: inline-block;
            padding: 15px 40px;
            background: var(--accent);
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-weight: 600;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        /* Section Manifeste */
        .manifesto {
            padding: 100px 10% ;
            background: var(--light);
            text-align: center;
        }

        .manifesto h2 {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            margin-bottom: 40px;
            color: var(--primary);
        }

        .manifesto-text {
            max-width: 800px;
            margin: 0 auto;
            font-size: 1.1rem;
            color: #555;
        }

        /* Cards Section */
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            padding: 80px 10%;
        }

        .card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
            border-bottom: 5px solid transparent;
        }

        .card:hover {
            transform: translateY(-10px);
            border-bottom: 5px solid var(--primary);
        }

        .card h3 {
            margin-bottom: 15px;
            color: var(--primary);
        }

        /* Footer */
        footer {
            padding: 50px;
            text-align: center;
            background: #222;
            color: rgba(255,255,255,0.6);
            font-size: 0.9rem;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .manifesto { padding: 60px 5%; }
            .features { padding: 40px 5%; }
        }
    </style>
</head>
<body>

    <section class="hero">
        <div class="hero-bg"></div>
        <div class="hero-content">
            <h1>Cuisiner, c'est s'aimer.</h1>
            <p>Redécouvrez le plaisir des produits simples, apprenez à ne plus rien jeter et transformez votre quotidien en festin.</p>
            <a href="#propos" class="btn">Découvrir l'aventure</a>
        </div>
    </section>

    <section class="manifesto" id="propos">
        <h2>Pourquoi ce projet ?</h2>
        <div class="manifesto-text">
            <p>Tout a commencé par un constat simple : nos poubelles débordent de produits oubliés, tandis que nos corps s'habituent au "vite-fait". On a voulu lancer ça pour prouver que <strong>bien manger</strong> n'est pas un luxe réservé aux chefs étoilés.</p>
            <br>
            <p>C'est une invitation à ralentir, à toucher les produits, à oser les associations et surtout, à respecter ce que la nature nous offre. Ici, on ne jette rien, on réinvente tout.</p>
        </div>
    </section>

    <section class="features">
        <div class="card">
            <h3>🥑 Pour vous</h3>
            <p>Reprenez le contrôle sur votre santé. Cuisiner soi-même, c'est savoir exactement ce qui compose votre énergie de demain.</p>
        </div>
        <div class="card">
            <h3>🌍 Anti-Gaspi</h3>
            <p>Apprenez à sublimer les restes et à cuisiner les parties oubliées des aliments. Moins de déchets, plus de goût.</p>
        </div>
        <div class="card">
            <h3>✨ Simplicité</h3>
            <p>Pas besoin de techniques compliquées. On prône le retour à l'essentiel : du bon, du frais, du vrai.</p>
        </div>
    </section>

    <footer>
        <p>&copy; 2026 - Créé avec passion pour les amoureux de la bonne bouffe.</p>
    </footer>

</body>
</html>
