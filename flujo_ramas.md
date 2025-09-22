
# Flujo sugerido de trabajo con ramas

En proyectos de Data Science se suelen manejar ramas de la siguiente forma:

- **main**: rama estable, con código limpio y reproducible.  
- **develop**: rama de integración donde se juntan las nuevas funcionalidades antes de pasar a producción.  
- **feature/**: ramas para nuevas funcionalidades o modelos validados.  
- **experiment/**: ramas para pruebas rápidas, hipótesis o prototipos (se pueden descartar si no sirven).  
- **hotfix/**: ramas para correcciones urgentes sobre `main`.  

---

## Ejemplo paso a paso

1. **Crear ramas base**
   ```bash
   git checkout -b develop main
   ```

2. **Crear una rama de experimento**
   ```bash
   git checkout develop
   git checkout -b experiment/random-forest
   ```
   Aquí trabajás con notebooks o pruebas iniciales.

3. **Hacer commits pequeños**
   ```bash
   git add notebooks/random_forest.ipynb
   git commit -m "experiment: implemento modelo random forest inicial"
   ```

4. **Validar resultados**
   - Si el experimento no funciona → se borra la rama.  
   - Si funciona → se limpia el código y se pasa a una rama `feature`.

5. **Crear una rama de feature**
   ```bash
   git checkout develop
   git checkout -b feature/random-forest-model
   ```

6. **Integrar en develop**
   ```bash
   git checkout develop
   git merge --squash feature/random-forest-model
   git commit -m "feature: agrego modelo random forest validado"
   ```

7. **Actualizar main**
   ```bash
   git checkout main
   git merge develop
   git tag -a v1.0 -m "Versión estable con Random Forest y XGBoost"
   ```

---

## Resumen del flujo
1. `experiment/` → pruebas y prototipos.  
2. `feature/` → integración de código validado.  
3. `develop` → integración de todas las features.  
4. `main` → rama estable y reproducible.  
