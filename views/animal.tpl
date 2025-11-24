<h1>Página Animal</h1> 
<p>Página destinada para os animais</p>

% for a in animals:
    <div style="background-color: {{ a.get('cor') }}; display: flex; align-items: center; justify-content: center; gap: 1rem">
        <h3>ID: </h3>
        <p>{{ a.get('id') }}</p>
        
        <h3>Nome: </h3>
        <p>{{ a.get('nome') }}</p>
        
        <h3>Raça: </h3>
        <p>{{ a.get('raca') }}</p>
    </div>
% end