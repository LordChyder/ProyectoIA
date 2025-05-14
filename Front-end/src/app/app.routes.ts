// app.routes.ts (principal de toda la app)
import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () =>
      import('./pages/inicio/inicio.component').then((m) => m.InicioComponent),
  },
  {
    path: 'voz',
    loadComponent: () =>
      import('./pages/voz/voz.component').then((m) => m.VozComponent),
  },
  {
    path: '**',
    redirectTo: '',
  },
];
