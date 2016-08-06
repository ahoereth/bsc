## Client
\label{sec:client_implementation}

### Redux

* Redux
* Zentraler Store
* Linearer Datenstrom

#### Actions

#### Reducers

#### Store

### React

* Komponenten Hierarchie
* Virtual DOM

```{.dot caption="\textbf{Home} component layout" label="components_home"}
digraph {
  HomeContainer -> Home;
  Home -> WelcomeMessage;
  Home -> LoginForm;
  Home -> LawList;
}
```

#### Container

* Interaktion mit Redux

#### Components

* *Dumme* Komponenten
* Weiß nichts von Redux --> leicht zu testen
* Zum großen Teil komplett state less -> leicht zu testen


\pagebreak

### Design

* Material Design
