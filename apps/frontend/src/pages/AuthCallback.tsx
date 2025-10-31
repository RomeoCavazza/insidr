import React, { useEffect } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { useAuth } from '@/contexts/AuthContext';

export default function AuthCallback() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const { setUser, setToken } = useAuth();

  useEffect(() => {
    const token = searchParams.get('token');
    const userId = searchParams.get('user_id');
    const email = searchParams.get('email');
    const name = searchParams.get('name');
    const error = searchParams.get('error');
    const errorDescription = searchParams.get('error_description');

    console.log('📥 AuthCallback - Paramètres reçus:', { 
      hasToken: !!token, 
      hasUserId: !!userId, 
      hasEmail: !!email,
      hasName: !!name,
      error,
      errorDescription
    });

    // Gérer les erreurs OAuth
    if (error) {
      console.error('❌ OAuth error:', error, errorDescription);
      // TODO: Afficher un toast d'erreur si disponible
      navigate('/auth?error=' + encodeURIComponent(errorDescription || error));
      return;
    }

    // Si on a un token, stocker immédiatement et rediriger vers /analytics
    // Le AuthContext chargera le user depuis le token au chargement de /analytics
    if (token) {
      // Décoder le token si nécessaire (il est URL-encodé)
      let decodedToken: string;
      try {
        decodedToken = decodeURIComponent(token);
      } catch (e) {
        // Si le décodage échoue, utiliser le token tel quel
        decodedToken = token;
      }
      
      console.log('🔑 Token décodé, longueur:', decodedToken.length);
      
      // Stocker le token immédiatement - C'EST TOUT CE QU'ON A BESOIN
      localStorage.setItem('token', decodedToken);
      setToken(decodedToken);
      
      // Si on a aussi userId/email dans l'URL, créer un user temporaire pour éviter ProtectedRoute
      if (userId && email) {
        const decodedEmail = email ? decodeURIComponent(email) : '';
        const decodedName = name ? decodeURIComponent(name) : '';
        setUser({
          id: parseInt(userId),
          email: decodedEmail,
          name: decodedName || decodedEmail.split('@')[0],
          role: 'user',
          created_at: new Date().toISOString(),
          is_active: true
        });
      }
      
      // Rediriger IMMÉDIATEMENT vers /analytics
      // Le AuthContext chargera le vrai user depuis /api/v1/auth/me au chargement
      console.log('🚀 Redirection immédiate vers /analytics');
      window.location.replace(window.location.origin + '/analytics');
      return;
    } else if (userId && email) {
      // Fallback: utiliser les paramètres URL si le token n'est pas dans l'URL
      // (cas où on stocke le token différemment)
      const decodedEmail = decodeURIComponent(email);
      const decodedName = name ? decodeURIComponent(name) : '';
      setUser({
        id: parseInt(userId),
        email: decodedEmail,
        name: decodedName || decodedEmail.split('@')[0],
        role: 'user',
        created_at: new Date().toISOString(),
        is_active: true
      });
      setTimeout(() => {
        console.log('🚀 Redirection vers /analytics (fallback userId)');
        window.location.href = '/analytics';
      }, 300);
    } else {
      // En cas d'erreur, rediriger vers la page de connexion
      console.error('Missing required parameters:', { token, userId, email });
      navigate('/auth?error=missing_params');
    }
  }, [searchParams, navigate, setUser, setToken]);

  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="text-center">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600 mx-auto"></div>
        <p className="mt-4 text-gray-600">Connexion en cours...</p>
      </div>
    </div>
  );
}
