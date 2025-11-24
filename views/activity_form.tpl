% rebase('layout.tpl', title='Nova Atividade' if not activity else 'Editar Atividade')


<h1>{{'Editar Atividade' if activity else 'Nova Atividade'}}</h1>
<form action="{{action}}" method="post">
    <label>Nome:<br>
        <input type="text" name="name" value="{{activity.name if activity else ''}}" required>
    </label><br><br>
    <label>Descrição:<br>
        <textarea name="description" required>{{activity.description if activity else ''}}</textarea>
    </label><br><br>
    <label>
        <input type="checkbox" name="done" % if activity and activity.done %checked% end>
        Feita?
    </label><br><br>
    <button type="submit">Salvar</button>
</form>
<a href="/activities">Voltar</a>