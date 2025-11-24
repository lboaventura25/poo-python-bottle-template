% rebase('layout.tpl', title='Atividades')


<h1>Atividades</h1>
<a href="/activities/add">Adicionar Atividade</a>
<table border="1">
    <tr>
        <th>ID</th><th>Nome</th><th>Descrição</th><th>Feita?</th><th>Ações</th>
    </tr>
    
    % for a in activities:
        <tr>
            <td>{{a.id}}</td>
            <td>{{a.name}}</td>
            <td>{{a.description}}</td>
            <td>{{'Sim' if a.done else 'Não'}}</td>
            <td>
                <a href="/activities/edit/{{a.id}}">Editar</a>
                <form action="/activities/delete/{{a.id}}" method="post" style="display:inline;">
                    <button type="submit">Excluir</button>
                </form>
            </td>
        </tr>
    % end
</table>